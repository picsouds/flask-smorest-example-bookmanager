"""Login resources"""
from datetime import datetime

from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, decode_token

from book_manager.extensions.api import Blueprint
from book_manager.models.schema import LoginQueryArgsSchema, JWTSchema

blp = Blueprint(
    'Auth',
    __name__,
    url_prefix='/auth',
    description="Auth for token JWT"
)


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@blp.route('/')
class Auth(MethodView):

    @blp.arguments(LoginQueryArgsSchema, location='query')
    @blp.response(JWTSchema, code=200)
    def post(self, args):
        """Obtenir un JWT Token"""
        username = args.pop('username', None)
        access_token = create_access_token(identity=username)
        pure_decoded = decode_token(access_token)
        return jsonify(access_token=access_token,
                       token_type='Bearer',
                       expires=datetime.fromtimestamp(pure_decoded["exp"]).strftime('%Y-%m-%d %H:%M:%S')), 200

