from http import HTTPStatus

from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity
)
from marshmallow import Schema, fields

blp = Blueprint("auth", __name__, url_prefix="/auth", description="Auth endpoints")


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


@blp.route("/login")
class Login(MethodView):
    @blp.doc(security=[])
    @blp.arguments(LoginSchema)
    def post(self, data):
        if data["username"] != "admin" or data["password"] != "secret":
            return {"msg": "Bad credentials"}, HTTPStatus.UNAUTHORIZED
        return {
            "access_token": create_access_token(identity=data["username"]),
            "refresh_token": create_refresh_token(identity=data["username"]),
        }, HTTPStatus.OK


@blp.route("/me")
class Me(MethodView):
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def get(self):
        return {"identity": get_jwt_identity()}, HTTPStatus.OK


@blp.route("/refresh")
class Refresh(MethodView):
    @blp.doc(security=[{"bearerAuth": []}])
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        return {"access_token": create_access_token(identity=identity)}, HTTPStatus.OK
