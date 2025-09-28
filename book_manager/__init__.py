"""Team Manager server application"""

from datetime import timedelta
from typing import Any, Mapping, Optional, Type

from flask import Flask
from flask_jwt_extended import JWTManager

from book_manager import extensions, views
from book_manager.default_settings import DefaultConfig


def create_app(
    config_object: Type[DefaultConfig] | str | None = None,
    config_overrides: Optional[Mapping[str, Any]] = None,
    **flask_kwargs: Any,
) -> Flask:
    """Create and configure the Flask application."""

    app = Flask(__name__, **flask_kwargs)
    app.json.sort_keys = False

    if config_object is None:
        config_object = DefaultConfig

    app.config.from_object(config_object)

    if config_overrides:
        app.config.from_mapping(config_overrides)

    # Override config with optional settings file from environment
    app.config.from_envvar('FLASK_SETTINGS_FILE', silent=True)
    app.config.setdefault("JWT_SECRET_KEY", "dev-secret-change-me")
    app.config.setdefault("JWT_ACCESS_TOKEN_EXPIRES", timedelta(seconds=3600))
    app.config.setdefault("JWT_REFRESH_TOKEN_EXPIRES", timedelta(seconds=604800))

    JWTManager(app)

    api = extensions.create_api(app)
    views.register_blueprints(api)

    return app
