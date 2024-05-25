from flask import Blueprint, request
from controllers.parameter import get_parameter_by_id, get_all_parameters, create_parameter, update_parameter, delete_parameter

parameter_routes = Blueprint('parameters', __name__)

@parameter_routes.route('/', methods=['GET'])
def get_all_parameters_route():
    return get_all_parameters()

@parameter_routes.route('/<int:id>', methods=['GET'])
def get_single_parameter_route(id):
    return get_parameter_by_id({'id': id})

@parameter_routes.route('/', methods=['POST'])
def create_new_parameter_route():
    return create_parameter(request.json)

@parameter_routes.route('/<int:id>', methods=['PUT'])
def update_existing_parameter_route(id):
    data = request.json
    data['id'] = id
    return update_parameter(data)

@parameter_routes.route('/<int:id>', methods=['DELETE'])
def delete_existing_parameter_route(id):
    return delete_parameter({'id': id})
