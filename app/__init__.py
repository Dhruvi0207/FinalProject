from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Use environment variable for database URI in production
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:admin@localhost/final_project')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: to disable Flask-SQLAlchemy event system

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
