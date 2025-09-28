"""Default configuration values for the Book Manager application."""

import os
import secrets
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

"""Default application settings"""


class DefaultConfig:
    """Default configuration"""

    API_VERSION = 0.1
    API_TITLE = "API_book_manager"
    OPENAPI_VERSION = "3.1.0"
    OPENAPI_URL_PREFIX = "/"

    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.17.14/"

    API_SPEC_OPTIONS = {
        "info": {
            "description": (
                "This is a sample server for the awesome "
                "[flask_smorest](https://flask-smorest.readthedocs.io/en/latest/)"
            ),
            "termsOfService": "http://helloreverb.com/terms/",
            "contact": {"email": "test@swagger.io"},
            "license": {
                "name": "MIT License",
                "url": "https://fr.wikipedia.org/wiki/Licence_MIT",
            },
        },
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
        "security": [{"bearerAuth": []}],
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(basedir, "app.db"))
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_ECHO = False

    #  if you feel specifying the order is important anyway.
    JSON_SORT_KEYS = False

    JWT_TOKEN_LOCATION = "headers"
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    JWT_SECRET_KEY = "super-secret"  # Change this!
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_ERROR_MESSAGE_KEY = "message"

    SECRET_KEY = secrets.token_urlsafe(16)
    WTF_CSRF_SECRET_KEY = secrets.token_urlsafe(16)
    WTF_CSRF_CHECK_DEFAULT = False
