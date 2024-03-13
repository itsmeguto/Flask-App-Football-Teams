from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

class Users(UserMixin, db.Model):  # Make sure to inherit from UserMixin!
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10))  # 'viewer' or 'admin'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
