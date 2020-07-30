"""CSRF"""

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def init_app(app):
    """Initialize JWT """
    csrf.init_app(app)
