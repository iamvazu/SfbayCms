#app/models
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """Create a Home table"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
