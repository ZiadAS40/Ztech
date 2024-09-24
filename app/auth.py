#!/usr/bin/python3
""" create the authentication routes """

from flask import Blueprint, render_template, redirect, request, flash, url_for, jsonify
from flask_jwt_extended import create_access_token
from flask_login import login_user, logout_user, current_user
from .models import User
from .routes import db
import json


auth = Blueprint('auth', __name__)

try:
    with open('users.json', 'r') as f:
        if f.read().strip() == "":
            users_orders = {}
        else:
            f.seek(0)
            users_orders = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    users_orders = {}


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
            try:
                with open('users.json', 'r') as f:
                    if f.read().strip() == "":
                        users_orders = {}
                    else:
                        f.seek(0)
                        users_orders = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                users_orders = {}          
            login_user(user)
            try:
                logout = users_orders['unknowen']
            except (KeyError):
                logout = {}
                print('no logout')
            try:
                login = users_orders[user.id]
            except (KeyError):
                login = {}
            
            if not login:
                print('no login')
            if logout:
                print('logout')

            if not login and logout:
                print('no login yes logout')
                users_orders[user.id] = users_orders['unknowen']
                del users_orders['unknowen']
            
            if login and logout:
                for order in login:
                    try:
                        sync_order = logout[order]
                    except (KeyError):
                        sync_order = []
                    login[order] = login[order] + sync_order
                
                for order in logout:
                    try:
                        sync_order = logout[order]
                    except (KeyError):
                        sync_order = []
                    if order not in login:
                        login[order] = []
                    login[order] = login[order] + sync_order
                del users_orders['unknowen']
            
                users_orders[user.id] = login
            
            with open('users.json', 'w') as f:
                json.dump(users_orders, f)
            
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