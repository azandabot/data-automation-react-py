from flask_cors import  cross_origin
from flask import Blueprint, request, jsonify
from controllers import get_device_by_id, get_device_total, get_all_devices, create_device, update_device, delete_device

device_routes = Blueprint('devices', __name__)

@device_routes.route('/', methods=['GET', 'POST'])
def get_all_devices_route():
    if request.method == 'GET':
        return get_all_devices()
    else: 
        return create_device(request.json)

@device_routes.route('/total', methods=['GET'])
def get_device_total_route():
    return get_device_total()

@device_routes.route('/<int:id>', methods=['GET'])
def get_single_device_route(id):
    return get_device_by_id({'id': id})


@device_routes.route('/<int:id>/', methods=['PUT'])
def update_existing_device_route(id):
    data = request.json
    data['id'] = id
    return update_device(data)

@device_routes.route('/<int:id>/', methods=['DELETE'])
def delete_existing_device_route(id):
    return delete_device({'id': id})
