#!/usr/bin/python3
""" create the authentication routes """

from flask import Blueprint, render_template, redirect, request, flash, url_for, jsonify
from flask_jwt_extended import create_access_token
from flask_login import login_user, logout_user, current_user
from .models import User
from .routes import db
import requests
auth = Blueprint('auth', __name__)


current_id = ''

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """adding the signup route"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        user_with_username = User.query.filter_by(username=username).first()
        user_with_email = User.query.filter_by(email=email).first()

        # if the username exists
        if user_with_username:
            flash('the user name already exist', 'error')
            return redirect(url_for('auth.signup'))
        
        # if the email exists
        if user_with_email:
            flash(f"email address already exitst\nplease choose different email", 'error')
            return redirect(url_for('auth.signup'))
        
        new_user = User(username, email)
        new_user.set_password(request.form['password'])

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))


    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        
        # validate the user and check the password
        if user and user.check_password(password):
            login_user(user)
            session_cookie = request.cookies.get('session')
            res = requests.post('http://127.0.0.1:5000/api/v1/sync', cookies={'session': session_cookie})
            if res.status_code == 201:
                print("POST request successful")
            else:
                print(f"POST request failed with status code: {res.status_code}")
            access_token = create_access_token(identity=user.id)
            res = {
                'access_token': access_token,
                'redirect_url': '/'
            }
            flash(f"welcome {username}", 'success')
            return jsonify(res)
        else:
            flash("wrong user name or password")
            return redirect (url_for('auth.login'))

    return render_template('login.html')


@auth.route('/logout', methods=['POST'])
def logout():
    """Logout user and clear session"""

    logout_user()

    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))