"""Pytest fixtures supporting Book Manager integration tests."""

import pytest
from sqlalchemy.pool import StaticPool

from book_manager import create_app
from book_manager.extensions.database import db


@pytest.fixture(scope="module")
def app():
    application = create_app(
        config_overrides={
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite+pysqlite:///:memory:",
            "DATABASE_URL": "sqlite+pysqlite:///:memory:",
            "SQLALCHEMY_ENGINE_OPTIONS": {
                "connect_args": {"check_same_thread": False},
                "poolclass": StaticPool,
            },
            "JWT_SECRET_KEY": "test-secret",
            "SECRET_KEY": "test-secret",
        }
    )

    ctx = application.app_context()
    ctx.push()

    yield application

    db.session.remove()
    ctx.pop()


@pytest.fixture(scope="module")
def test_client(app):
    with app.test_client() as testing_client:
        yield testing_client
