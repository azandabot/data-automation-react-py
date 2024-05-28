from utils import execute_stmt
from models import Devices

def get_device_total():
    return execute_stmt(Devices, {}, 'GET_TOTAL')

def get_device_by_id(device_id):
    return execute_stmt(Devices, {'id': device_id}, 'GET_SINGLE')

def get_all_devices():
    return execute_stmt(Devices, {}, 'GET_ALL')

def create_device(data):
    return execute_stmt(Devices, data, 'POST')

def update_device(data):
    return execute_stmt(Devices, data, 'PUT')

def delete_device(device_id):
    return execute_stmt(Devices, {'id': device_id}, 'DELETE')
