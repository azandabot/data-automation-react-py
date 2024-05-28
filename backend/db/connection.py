from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def create_database(app):
    with app.app_context():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        if not tables:  # If no tables exist, create them
            db.create_all()
            print("Database tables created.")
        else:
            print("Database tables already exist.")