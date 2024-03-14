from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    csrf = CSRFProtect(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    
    from app.views.auth import auth
    app.register_blueprint(auth, url_prefix="/auth")
    
    from app.views.main import main
    app.register_blueprint(main)
    
    # Auth Steps
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.users import User  # Ensure this matches your project structure
        return User.query.get(int(user_id))
    
    with app.app_context():
        return app