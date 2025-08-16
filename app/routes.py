from . import app
from flask import render_template, redirect, flash, request

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
    return render_template('login.html', title='Login')

@app.route('/signup')
def signup():
    
    return render_template('signup.html', title='Registration')

