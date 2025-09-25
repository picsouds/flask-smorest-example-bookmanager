"""Api extension initialization

Override base classes here to allow painless customization in the future.
"""
from flask_smorest import Api as ApiOrig, Blueprint as BlueprintOrig
from flask_smorest.pagination import Page


class Blueprint(BlueprintOrig):
    """Blueprint override"""


class Api(ApiOrig):
    """Api override"""

    def __init__(self, app=None, *, spec_kwargs=None):
        spec_kwargs = spec_kwargs or {}
        super().__init__(app, spec_kwargs=spec_kwargs)
        self.spec.components.security_scheme("bearerAuth", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"})


class SQLCursorPage(Page):
    """SQL cursor pager"""

    # https://flask-smorest.readthedocs.io/en/latest/pagination.html
    @property
    def item_count(self):
        return self.collection.count()
