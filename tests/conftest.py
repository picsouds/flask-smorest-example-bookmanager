import pytest

from book_manager import create_app


@pytest.fixture(scope='module')
def test_client():
    application = create_app()
    application.config['TESTING'] = True

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = application.test_client()

    # Establish an application context before running the tests.
    ctx = application.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
