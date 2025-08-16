from flask import Flask
from config import Config
from .extensions import db, migrate, csrf

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app,db)
csrf.init_app(app)

from .routes import *
from .models import User