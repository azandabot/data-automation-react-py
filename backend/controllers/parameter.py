from utils import execute_stmt
from models import Parameters

def get_least_frequent_parameter():
   return execute_stmt(Parameters, { 'LEAST' }, 'GET_FREQUENCY')

def get_most_frequent_parameter():
   return execute_stmt(Parameters, { 'MOST' }, 'GET_FREQUENCY')

def get_top_10_parameters():
   return execute_stmt(Parameters, { 'TOP_10' }, 'GET_CHART')

def get_device_parameter_split():
   return execute_stmt(Parameters, { 'GET_WITH_DEVICE_NAME_AND_PARAM_COUNT' }, 'GET_CHART')

def get_parameter_by_id(parameter_id):
    params = {'id': parameter_id}
    return execute_stmt(Parameters, params, 'GET_SINGLE')

def get_all_parameters():
    return execute_stmt(Parameters, {}, 'GET_ALL')

def get_total_parameters():
    return execute_stmt(Parameters, {}, 'GET_TOTAL')

def create_parameter(parameter_data):
    parameter_data['type'] = 'numeric' if parameter_data['value'].isdigit() else 'text'
    return execute_stmt(Parameters, parameter_data, 'POST')

def update_parameter(updated_data):
    return execute_stmt(Parameters, updated_data, 'PUT')

def delete_parameter(parameter_id):
    params = {'id': parameter_id}
    return execute_stmt(Parameters, params, 'DELETE')
