"""Team Manager server application"""

from flask import Flask

from book_manager import extensions, views
from book_manager.default_settings import DefaultConfig


def create_app():
    """Create application"""
    app = Flask(__name__)

    app.config.from_object(DefaultConfig)
    # Override config with optional settings file
    app.config.from_envvar('FLASK_SETTINGS_FILE', silent=True)

    api = extensions.create_api(app)
    views.register_blueprints(api)

    return app
