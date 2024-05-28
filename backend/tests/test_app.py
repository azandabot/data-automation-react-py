import json
import pytest
import uuid
from app import app as flask_app
from models import Users, Devices, Parameters
from db import db, seed_db

@pytest.fixture(scope='module')
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
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
    return app.test_client()

def test_seed_db(app):
    with app.app_context():
        user = Users.query.filter_by(username="REACT_APP").first()
        assert user is not None
        assert Devices.query.count() > 0
        assert Parameters.query.count() > 0

def test_get_devices(client):
    response = client.get('/devices/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_create_device(client):
    new_device = {
        'name': 'test 123',
        'active': 'Y'
    }
    response = client.post('/devices', data=json.dumps(new_device), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == new_device['name']

def test_update_device(client):
    device = Devices.query.first()
    if device:
        updated_data = {
            'id': device.id,
            'name': 'Updated Device'
        }
        response = client.put(f'/devices/{device.id}', data=json.dumps(updated_data), content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == updated_data['name']

def test_delete_device(client):
    device = Devices.query.first()
    if device:
        response = client.delete(f'/devices/{device.id}')
        assert response.status_code == 204
        assert Devices.query.get(device.id) is None

def test_get_parameters(client):
    response = client.get('/parameters')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_create_parameter(client):
    device = Devices.query.first()
    if device:
        new_parameter = {
            'device_id': device.id,
            'name': 'New Parameter',
            'value': '100',
            'type': 'numeric',
            'created_at': '2023-05-27T00:00:00Z',
            'updated_at': '2023-05-27T00:00:00Z'
        }
        response = client.post('/parameters', data=json.dumps(new_parameter), content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == new_parameter['name']

def test_update_parameter(client):
    parameter = Parameters.query.first()
    if parameter:
        updated_data = {
            'id': parameter.id,
            'name': 'Updated Parameter'
        }
        response = client.put(f'/parameters/{parameter.id}', data=json.dumps(updated_data), content_type='application/json')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == updated_data['name']

def test_delete_parameter(client):
    parameter = Parameters.query.first()
    if parameter:
        response = client.delete(f'/parameters/{parameter.id}')
        assert response.status_code == 204
        assert Parameters.query.get(parameter.id) is None
