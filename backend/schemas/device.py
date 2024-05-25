from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.device import Devices

class DeviceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Devices
        load_instance = True

    id = fields.Int(dump_only=True)
    user_token = fields.UUID(required=True)
    name = fields.Str(required=True)
    active = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
