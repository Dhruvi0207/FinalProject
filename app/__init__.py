from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration from config.py

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
