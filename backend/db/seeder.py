from models import Users, Devices, Parameters
from sqlalchemy import inspect
from db.connection import db
import json
import uuid

def seed_db():
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()
    
    if not set(['users', 'devices', 'parameters']).issubset(set(table_names)):
        db.create_all()

        user = Users(username="REACT_APP", token=uuid.uuid4())
        db.session.add(user)
        db.session.commit()

        # Seed devices and parameters
        with open('seed/sample.json') as f:
            devices_data = json.load(f)
            for device_name, parameters in devices_data.items():
                # Check if device already exists
                device = Devices.query.filter_by(name=device_name).first()
                if not device:
                    # Create a new device if it doesn't exist
                    device = Devices(user_token=user.token, name=device_name)
                    db.session.add(device)
                    db.session.commit()
                
                for param in parameters:
                    # Create a new parameter if it doesn't exist
                    parameter = Parameters(
                        device_id=device.id,
                        name=param["parameter"],
                        type=param["type"],
                        value=param["value"],
                        created_at=param["timestamp"],
                        updated_at=param["timestamp"]
                    )
                    db.session.add(parameter)
                    db.session.commit()
