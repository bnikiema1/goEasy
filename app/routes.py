from . import app

@app.route('/')
def login():
    return 'Login'