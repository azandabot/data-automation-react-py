from db import db
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    token = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False, unique=True)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=True, default=None)

    __table_args__ = (UniqueConstraint('token', name='uq_users_token'),)
