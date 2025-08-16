from flask import Flask
from config import Config
from .extensions import db, migrate, csrf, bcrypt, login_manager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app,db)
csrf.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = '/'

from .routes import *
from .models import User