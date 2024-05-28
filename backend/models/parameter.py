from db import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID, JSON

class Parameters(db.Model):
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('devices.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(50), nullable=False)
    type = Column(String(10), nullable=False, default='numeric')
    value = Column(JSON, nullable=False)  # Using JSON to store both numeric and text values
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


    def serialize(self, include_device_name=False):
        """
        Serialize the parameters object into a dictionary.
        """
        serialized_data = {
            'id': self.id,
            'device_id': self.device_id,
            'name': self.name,
            'type': self.type,
            'value': self.value,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }

        if include_device_name:
            # Include device name if required
            serialized_data['device_name'] = self.device.name  # Assuming there's a relationship 'device' in Parameters model

        return serialized_data