"""Modules initialization"""

from . import books
from . import authors
from . import auth

MODULES = (
    auth,
    authors,
    books
)


def register_blueprints(api):
    """Initialize application with all modules"""
    for module in MODULES:
        api.register_blueprint(module.blp)
