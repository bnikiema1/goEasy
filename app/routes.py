from . import app
from flask import render_template, redirect, flash, request

@app.route('/')
def login():
    
    return render_template('login.html', title='Login')

@app.route('/signup')
def signup():
    
    return render_template('signup.html', title='Registration')

