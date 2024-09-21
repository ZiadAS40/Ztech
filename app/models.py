#!/usr/bin/python3
"""Making the database models"""

from .routes import db
import uuid
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Implementing the user model"""
    id = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(255))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __init__(self, username, email):
        """intialize the user object"""
        self.username = username
        self.email = email
        self.id = uuid.uuid4()

