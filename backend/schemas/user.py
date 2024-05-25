from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.user import Users

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True

    id = fields.Int(dump_only=True)
    token = fields.UUID(dump_only=True)
    username = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
