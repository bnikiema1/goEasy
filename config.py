import os
from pathlib import Path

base_dir = Path(__file__).parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'project.db')
    
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('CSRF_SECRET_KEY') or 'csrf key'