"""Modules initialization"""

from . import books
from . import authors
from .auth.resources import blp as authblp

MODULES = (
    authors,
    books,
)


def register_blueprints(api):
    """Initialize application with all modules"""
    api.register_blueprint(authblp)
    for module in MODULES:
        api.register_blueprint(module.blp)
