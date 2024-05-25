from flask import Flask
from config import DATABASE_URL
from db import db, create_database, seed_db
from flask_migrate import Migrate
from routes import init_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        create_database(app)  # Create all database tables
        seed_db()  # Seed initial data
        init_routes(app)  # Initialize routes
        app.run(debug=True)
