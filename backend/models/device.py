from db import db
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

class Devices(db.Model):
    id = Column(Integer, primary_key=True)
    user_token = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(50), nullable=False, unique=True)
    active = Column(String(1), default='Y', nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime)

    def serialize(self):
        """
        Serialize the device object into a dictionary.
        """
        return {
            'id': self.id,
            'user_token': str(self.user_token),
            'name': self.name,
            'active': self.active,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
