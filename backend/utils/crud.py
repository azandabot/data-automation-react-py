from flask import jsonify
from db import db
from models import Devices
from sqlalchemy import func


def serialize_parameter_with_device_and_count(parameter, device_name, param_count):
    serialized_parameter = parameter.serialize()
    serialized_parameter['device_name'] = device_name
    serialized_parameter['param_count'] = param_count
    return serialized_parameter


def execute_stmt(model, params, operation):
    """
    Perform CRUD operation based on the given parameters.

    Args:
        model (SQLAlchemy model class): The model class representing the database table.
        params (dict): Dictionary containing parameters for the operation.
        operation (str): Operation type (GET_SINGLE, GET_ALL, POST, PUT, DELETE).

    Returns:
        Tuple: Tuple containing Response message, Status code, JSON response.
    """

    # Perform operation based on operation type
    if operation == 'GET_SINGLE':
        # Get a single record by ID
        record_id = params.get('id')
        record = model.query.get(record_id)
        if record:
            return jsonify({
                'request_method': 'GET',
                'message': 'Records fetched successfully!',
                'data': record.serialize()
            }), 200
        else:
            return jsonify({'message': 'Record not found'}), 404
    
    elif operation == 'GET_ALL':
        if 'id' in params:
            records = model.query.filter_by(id=params['id']).all()
        else:
            records = model.query.all()
        
        return jsonify({ 
            'request_method': 'GET', 
            'message': 'Records fetched successfully!', 
            'data': [record.serialize() for record in records]
        }), 200
    
    elif operation == 'GET_FREQUENCY':
        if 'MOST' in params:
            result = db.session.query(
                        model.name, func.count(model.name).label('count')
                    ).group_by(model.name).order_by(func.count(model.name)).first()
        else:
          result = db.session.query(
                        model.name, func.count(model.name).label('count')
                    ).group_by(model.name).order_by(func.count(model.name).desc()).first()
        
        return jsonify({ 
            'request_method': 'GET', 
            'message': 'Records fetched successfully!', 
            'data': result[0] + ": " + str(result[1]) 
        }), 200
    
    elif operation == 'GET_TOTAL':
        total = db.session.query(func.count(model.id)).scalar()
        
        return jsonify({ 
            'request_method': 'GET', 
            'message': 'Total Fetched successfully!', 
            'data': total
        }), 200
    
    elif operation == 'GET_CHART':
        if 'TOP_10' in params:
            result = db.session.query(
                model.name, func.count(model.name).label('count')
            ).group_by(model.name).order_by(func.count(model.name)).limit(10)
            result = [{
                'name': row.name,
                'total': row.count
            } for row in result]

        else:
            result = db.session.query(
                    Devices.name.label('device_name'),
                    func.count(model.id).label('total')
                ).outerjoin(model, Devices.id == model.device_id).group_by(Devices.id).limit(10).all()
            result = [{
                'name': row.device_name,
                'total': row.total
            } for row in result]

        return jsonify({ 
            'request_method': 'GET', 
            'message': 'Total Fetched successfully!', 
            'data': result
        }), 200

    elif operation == 'POST':
        if model == Devices:
            # Check if record already exists
            existing_record = model.query.filter_by(**params).first()
            if existing_record:
                return jsonify({
                    'request_method': 'POST',
                    'message': 'Device already exists'
                }), 409
        # Create a new record
        new_record = model(**params)
        db.session.add(new_record)
        db.session.commit()
        return jsonify({
            'request_method': 'POST',
            'message': 'Record saved successfully!'
        }), 201


    
    elif operation == 'PUT':
        # Update an existing record
        record_id = params.pop('id')
        record = model.query.get(record_id)
        if record:
            for key, value in params.items():
                setattr(record, key, value)
            db.session.commit()
            return jsonify({
                'request_method': 'PUT',
                'message': 'Record updated successfully'
            }), 200
        else:
            return jsonify({
                'request_method': 'PUT',
                'message': 'Record not found'
            }), 404
    
    elif operation == 'DELETE':
        # Delete a record
        record_id = params.get('id')
        record = model.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return jsonify({
                'request_method': 'DELETE',
                'message': 'Record deleted successfully'
            }), 200
        else:
            return jsonify({'message': 'Record not found'}), 404
    
    else:
        return jsonify({
            'request_method': 'INVALID',
            'message': 'Invalid operation'
        }), 400
