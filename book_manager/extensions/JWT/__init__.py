"""JWT"""

from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_app(app):
    """Initialize JWT"""
    jwt.init_app(app)
