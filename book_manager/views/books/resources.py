"""Books resources"""

from uuid import UUID

from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from book_manager.extensions.api import Blueprint, SQLCursorPage
from book_manager.extensions.database import db
from book_manager.models import Book
from book_manager.models.schema import BookQueryArgsSchema, BookSchema

blp = Blueprint("Books", __name__, url_prefix="/books", description="Opérations sur les livres")


def _get_book_or_404(item_id: UUID) -> Book:
    """Return the book or abort with 404."""
    instance = db.session.get(Book, item_id)
    if instance is None:
        abort(404, message=f"Book {item_id} not found")
    return instance


@blp.route("/")
class Books(MethodView):
    """Collection-level operations for ``Book`` resources."""

    @blp.etag
    @blp.arguments(BookQueryArgsSchema, location="query")
    @blp.response(200, BookSchema(many=True))
    @blp.paginate(SQLCursorPage)
    def get(self, args):
        """List des livres"""
        return Book.query.filter_by(**args)

    @blp.etag
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def post(self, new_item):
        """Ajouter un nouveau livre"""
        item = Book(**new_item)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(
                400,
                message=e.__class__.__name__,
                errors="author_id {} not found".format(item.author_id),
            )
        except SQLAlchemyError as e:
            db.session.rollback()
            message = [str(x) for x in e.args]
            abort(400, message=e.__class__.__name__, errors=message)

        return item


@blp.route("/<uuid:item_id>")
class BooksById(MethodView):

    @blp.etag
    @blp.response(200, BookSchema)
    def get(self, item_id):
        """Livre par ID"""
        return _get_book_or_404(item_id)

    @blp.etag
    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    @blp.doc(parameters=[{"name": "If-Match", "in": "header", "required": "true"}])
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def put(self, new_item, item_id):
        """Modifier un livre existant par ID"""
        item = _get_book_or_404(item_id)
        blp.check_etag(item, BookSchema)
        try:
            BookSchema().update(item, new_item)
            db.session.add(item)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(
                400,
                message=e.__class__.__name__,
                errors="author_id {} not found".format(new_item["author_id"]),
            )
        except SQLAlchemyError as e:
            db.session.rollback()
            message = [str(x) for x in e.args]
            abort(400, message=e.__class__.__name__, errors=message)

        return item

    @blp.etag
    @blp.response(204)
    @blp.doc(parameters=[{"name": "If-Match", "in": "header", "required": "true"}])
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def delete(self, item_id):
        """Supprimer un livre par ID"""
        item = _get_book_or_404(item_id)
        blp.check_etag(item, BookSchema)
        db.session.delete(item)
        db.session.commit()
