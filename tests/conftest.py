import pytest
from greetings_app.entrypoints import app


@pytest.fixture
def client():
    flask_app = app.create_app()
    flask_app.config["TESTING"] = True
    client = flask_app.test_client()
    yield client
