"""Modules initialization"""

from . import books
from . import authors
from .auth.resources import blp as AuthBlp

MODULES = (
    authors,
    books,
)


def register_blueprints(api):
    """Initialize application with all modules"""
    api.register_blueprint(AuthBlp)
    for module in MODULES:
        api.register_blueprint(module.blp)
