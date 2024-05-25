from flask import Blueprint, request, jsonify
from controllers import get_device_by_id, get_all_devices, create_device, update_device, delete_device

device_routes = Blueprint('devices', __name__)

@device_routes.route('/', methods=['GET'])
def get_all_devices_route():
    return get_all_devices()

@device_routes.route('/<int:id>', methods=['GET'])
def get_single_device_route(id):
    return get_device_by_id({'id': id})

@device_routes.route('/', methods=['POST'])
def create_new_device_route():
    return create_device(request.json)

@device_routes.route('/<int:id>', methods=['PUT'])
def update_existing_device_route(id):
    data = request.json
    data['id'] = id
    return update_device(data)

@device_routes.route('/<int:id>', methods=['DELETE'])
def delete_existing_device_route(id):
    return delete_device({'id': id})
