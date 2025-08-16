from . import app
from.extensions import db
from .models import User
from flask import render_template, redirect, flash, request, url_for
from flask_login import login_required, current_user, logout_user, login_user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user != None:
            if user.check_hash(request.form['password']):
                login_user(user, remember=False)
                return redirect(url_for('dashboard'))
        else:
            print("incorrect username or password")
            return redirect(url_for('login'))
    return render_template('login.html', title='Login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        if request.form['password'] == request.form['confirmed']:
            user = User(username= request.form['username'], email=request.form['email'])
            user.pass_hash(request.form['password'])
            db.session.add(user)
            db.session.commit()
            print(f' Account created for {user.username}')
            return redirect(url_for('login'))
        else:
            print('passwords dont match')
            return redirect(url_for('signup'))
            
    return render_template('signup.html', title='Registration')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('User/dashboard.html', title='Dashboard')

