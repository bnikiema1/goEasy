from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True, index=True)
    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    password = db.Column(db.String(80))
    