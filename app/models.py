from .extensions import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True, index=True)
    email = db.Column(db.String(80), nullable=False, unique=True, index=True)
    password = db.Column(db.String(80))
    
    def pass_hash(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
    
    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'ID: {self.id}, Username: {self.username}, Email: {self.email}'
