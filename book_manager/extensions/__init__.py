"""Extensions initialization"""

from . import database, JWT, csrf
from .api import Api


def create_api(app):
    """Init extension"""
    new_api = Api(app)

    for extension in (database, JWT, csrf):
        extension.init_app(app)

    return new_api
