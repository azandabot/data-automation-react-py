from utils import execute_stmt
from models import Parameters

def get_parameter_by_id(parameter_id):
    params = {'id': parameter_id}
    return execute_stmt(Parameters, params, 'GET_SINGLE')

def get_all_parameters():
    return execute_stmt(Parameters, {}, 'GET_ALL')

def create_parameter(parameter_data):
    return execute_stmt(Parameters, parameter_data, 'POST')

def update_parameter(parameter_id, updated_data):
    updated_data['id'] = parameter_id
    return execute_stmt(Parameters, updated_data, 'PUT')

def delete_parameter(parameter_id):
    params = {'id': parameter_id}
    return execute_stmt(Parameters, params, 'DELETE')
