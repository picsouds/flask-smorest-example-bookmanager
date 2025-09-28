import marshmallow as mar
from marshmallow import EXCLUDE
from marshmallow.validate import Length
from marshmallow_sqlalchemy import field_for, SQLAlchemySchema

from book_manager.models import Book, Author


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        ordered = True
        #        include_fk = True
        unknown = EXCLUDE

    id = field_for(Book, "id", dump_only=True)
    title = field_for(Book, "title", required=True, validate=Length(min=1))
    author_id = field_for(Book, "author_id", required=True)
    created_at = field_for(Author, "created_at", dump_only=True)
    updated_at = field_for(Author, "updated_at", dump_only=True)

    def update(self, obj, data):
        """Update object nullifying missing data"""
        loadable_fields = [k for k, v in self.fields.items() if not v.dump_only]
        for name in loadable_fields:
            setattr(obj, name, data.get(name))


class BookQueryArgsSchema(mar.Schema):
    class Meta:
        unknown = EXCLUDE

    name = mar.fields.Str()
    title = mar.fields.Str()
    author_id = mar.fields.UUID()


class AuthorSchema(SQLAlchemySchema):
    class Meta:
        model = Author
        ordered = True
        unknown = EXCLUDE
        dateformat = "%Y-%m-%d"

    id = field_for(Author, "id", dump_only=True)
    first_name = field_for(Author, "first_name", required=True, validate=Length(min=2, max=40))
    last_name = field_for(Author, "last_name", required=True, validate=Length(min=2, max=40))
    birth_date = field_for(Author, "birth_date", required=True)
    created_at = field_for(Author, "created_at", dump_only=True)
    updated_at = field_for(Author, "updated_at", dump_only=True)

    def update(self, obj, data):
        """Update object nullifying missing data"""
        loadable_fields = [k for k, v in self.fields.items() if not v.dump_only]
        for name in loadable_fields:
            setattr(obj, name, data.get(name))


class AuthorQueryArgsSchema(mar.Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    first_name = mar.fields.Str(validate=Length(min=2, max=40))
    last_name = mar.fields.Str(validate=Length(min=2, max=40))


class LoginQueryArgsSchema(mar.Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    user = mar.fields.Str(required=True, validate=Length(min=2, max=40))
    password = mar.fields.Str(required=True, validate=Length(min=2, max=40))


class JWTSchema(mar.Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    access_token = mar.fields.Str()
    token_type = mar.fields.Str()
    expires = mar.fields.Str()
