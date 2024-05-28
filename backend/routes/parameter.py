from flask import Blueprint, request
from controllers.parameter import get_top_10_parameters, get_device_parameter_split, get_least_frequent_parameter, get_most_frequent_parameter, get_parameter_by_id, get_total_parameters, get_all_parameters, create_parameter, update_parameter, delete_parameter

parameter_routes = Blueprint('parameters', __name__)

@parameter_routes.route('/', methods=['GET'])
def get_all_parameters_route():
    return get_all_parameters()

@parameter_routes.route('/device/parameter/split', methods=['GET'])
def get_device_parameter_split_route():
    return get_device_parameter_split()

@parameter_routes.route('/top/10/parameters', methods=['GET'])
def get_top_10_parameters_route():
    return get_top_10_parameters()

@parameter_routes.route('/total', methods=['GET'])
def get_total_parameters_route():
    return get_total_parameters()

@parameter_routes.route('/frequent/most', methods=['GET'])
def get_most_frequent_param_route():
    return get_most_frequent_parameter()

@parameter_routes.route('/frequent/least', methods=['GET'])
def get_least_frequent_param_route():
    return get_least_frequent_parameter()

@parameter_routes.route('/<int:id>/', methods=['GET'])
def get_single_parameter_route(id):
    return get_parameter_by_id({'id': id})

@parameter_routes.route('/', methods=['POST'])
def create_new_parameter_route():
    return create_parameter(request.json)

@parameter_routes.route('/<int:id>/', methods=['PUT'])
def update_existing_parameter_route(id):
    data = request.json
    data['id'] = id
    if(data['value']):
        data['type'] = 'numeric' if data['value'].isdigit() else 'text'

    return update_parameter(data)

@parameter_routes.route('/<int:id>/', methods=['DELETE'])
def delete_existing_parameter_route(id):
    return delete_parameter({'id': id})
