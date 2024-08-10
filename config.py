import os

class Config:
    # Basic Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'f5d6e3d2c1a2b3c4d5e6f7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z')  
    
    # SQLAlchemy Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:admin@localhost/final_project')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
