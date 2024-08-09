import os

class Config:
    # Basic Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Use an environment variable or default value
    
    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:admin@localhost/final_project')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
