from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize the database extension without an app
db = SQLAlchemy()

def create_app():
    # Create a Flask instance
    app = Flask(__name__)
    # Configuration settings for your app, can be from a class or file
    app.config.from_object('config.Config')
    
    # Initialize plugins
    db.init_app(app)
    
    # Initialize dat migrations
    migrate = Migrate(app, db)

    # You can import models here if necessary, but avoid circular imports
    from .models import leagues
    
    # Import and register your Blueprints here
    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
