"""Authors resources"""
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from book_manager.extensions.api import Blueprint, SQLCursorPage
from book_manager.extensions.database import db
from book_manager.models import Author, Book
from book_manager.models.schema import AuthorSchema, AuthorQueryArgsSchema

blp = Blueprint(
    'Authors',
    __name__,
    url_prefix='/authors',
    description="Operations sur les auteurs"
)


@blp.route('/')
class Authors(MethodView):

    @blp.etag
    @blp.arguments(AuthorQueryArgsSchema, location='query')
    @blp.response(AuthorSchema(many=True))
    @blp.paginate(SQLCursorPage)
    def get(self, args):
        """Liste des auteurs"""
        book_id = args.pop('book_id', None)
        ret = Author.query.filter_by(**args)
        if book_id is not None:
            ret = ret.join(Author.books).filter(Book.id == book_id)
        return ret

    @blp.etag
    @blp.arguments(AuthorSchema, example=dict(first_name="John", last_name="Doe", birth_date="1900-01-01"))
    @blp.response(AuthorSchema, code=201)
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required
    def post(self, new_item):
        """Ajouter un nouvel auteur"""

        # Access the identity of the current author with get_jwt_identity
        # current_author = get_jwt_identity()

        item = Author(**new_item)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route('/<uuid:item_id>')
class AuthorsById(MethodView):

    @blp.etag
    @blp.response(AuthorSchema)
    def get(self, item_id):
        """Auteur par ID"""
        return Author.query.get_or_404(item_id)

    @blp.etag
    @blp.arguments(AuthorSchema)
    @blp.response(AuthorSchema)
    @blp.doc(parameters=[{'name': 'If-Match', 'in': 'header', 'required': 'true'}])
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required
    def put(self, new_item, item_id):
        """Modifier un auteur existant par ID"""
        item = Author.query.get_or_404(item_id)
        blp.check_etag(item, AuthorSchema)
        AuthorSchema().update(item, new_item)
        db.session.add(item)
        db.session.commit()
        return item

    @blp.etag
    @blp.response(code=204)
    @blp.doc(parameters=[{'name': 'If-Match', 'in': 'header', 'required': 'true'}])
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required
    def delete(self, item_id):
        """Supprimer un auteur par ID"""
        item = Author.query.get_or_404(item_id)
        blp.check_etag(item, AuthorSchema)
        db.session.delete(item)
        db.session.commit()
