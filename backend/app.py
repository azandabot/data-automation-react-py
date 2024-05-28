from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import DATABASE_URL
from db import db, seed_db
from routes import init_routes

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        seed_db()  # Seed initial data if tables don't exist
          # Initialize routes
        app.run(debug=True)