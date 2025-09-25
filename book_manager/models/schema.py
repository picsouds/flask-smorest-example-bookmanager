from marshmallow import EXCLUDE, Schema, fields
from marshmallow.validate import Length


class NullMissingMixin:
    """Helper mixin to normalise missing field updates."""

    def update(self, obj, data):
        loadable_fields = [name for name, field in self.fields.items() if not field.dump_only]
        for name in loadable_fields:
            setattr(obj, name, data.get(name))


class BookSchema(NullMissingMixin, Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    id = fields.UUID(dump_only=True)
    title = fields.Str(required=True, validate=Length(min=1))
    author_id = fields.UUID(required=True, data_key="author_id")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookQueryArgsSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str()
    title = fields.Str()
    author_id = fields.UUID()


class AuthorSchema(NullMissingMixin, Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    id = fields.UUID(dump_only=True)
    first_name = fields.Str(required=True, validate=Length(min=2, max=40))
    last_name = fields.Str(required=True, validate=Length(min=2, max=40))
    birth_date = fields.Date(required=True, format="iso")
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class AuthorQueryArgsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    first_name = fields.Str(validate=Length(min=2, max=40))
    last_name = fields.Str(validate=Length(min=2, max=40))
    book_id = fields.UUID(load_only=True)


class LoginQueryArgsSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    user = fields.Str(required=True, validate=Length(min=2, max=40))
    password = fields.Str(required=True, validate=Length(min=2, max=40))


class JWTSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    access_token = fields.Str()
    token_type = fields.Str()
    expires = fields.Str()
