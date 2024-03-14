import os

class Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-long-and-unique-key'

    # Database configuration
    # Note: Replace 'your_username', 'your_password', 'your_database', and 'your_host' with your actual database credentials and MySQL host.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:admin1234.@localhost/football_manager'
    
    # This setting is used to suppress a warning that SQLAlchemy gives if this is not set.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add any other configuration variables here

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:admin1234.@localhost/football_manager'
    WTF_CSRF_ENABLED = False  # Disable CSRF forms protection in testing