import pytest
from app import create_app
from app.models import db

@pytest.fixture
def app():
    """Create application instance for testing."""
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        try:
            db.drop_all()
        except Exception:
            pass

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
