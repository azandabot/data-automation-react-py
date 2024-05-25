from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.parameter import Parameters

class ParameterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Parameters
        load_instance = True

    id = fields.Int(dump_only=True)
    device_id = fields.Int(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    value = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
