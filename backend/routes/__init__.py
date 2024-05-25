from flask import Blueprint
from .device import device_routes
from .parameter import parameter_routes

def init_routes(app):
    # Register the blueprints for the different route groups
    app.register_blueprint(device_routes, url_prefix='/devices')
    app.register_blueprint(parameter_routes, url_prefix='/parameters')