import pytest

from config import TEST_DATABASE_URL
from app import app as flask_app
from db import db, seed_db

@pytest.fixture(scope='module')
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URL
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with flask_app.app_context():
        db.create_all()
        seed_db()  # Seed initial data if tables don't exist

    yield flask_app

    with flask_app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as client:
        yield client
