from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect


# Initialize the database extension without an app
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'  # Specify the view that handles logins

def create_app():
    # Create a Flask instance
    app = Flask(__name__)
    # Configuration settings for your app, can be from a class or file
    app.config.from_object('config.Config')
    csrf = CSRFProtect(app)
        
    # Initialize plugins
    db.init_app(app)
    
    # Initialize dat migrations
    migrate = Migrate(app, db)
    
    from .models import leagues
    from .models.users import Users
    
    # Import and register your Blueprints here
    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Auth Steps
    login_manager.init_app(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models.users import Users
    
    return Users.query.get(int(user_id))