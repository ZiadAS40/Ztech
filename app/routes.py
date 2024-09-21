#!/user/bin/python3
""" the main app routes """


from flask import Flask, make_response, jsonify, render_template, url_for, request

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager 
import requests
from flask_login import current_user, login_required   
from datetime import timedelta

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ziad4036:ltstore@localhost/lt_store'
app.config['SECRET_KEY'] = 'sec-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}}, supports_credentials=True)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
jwt = JWTManager(app)

def configure_app():
    from api.v1.views import app_views
    from .auth import auth
    app.register_blueprint(app_views, url_prefix='/api/v1')
    app.register_blueprint(auth, url_prefix='/')



@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@login_manager.user_loader
def load_user(user_id):
    """implement the session manager"""
    from .models import User
    return User.query.get(user_id)

@app.route('/')
def homePage():
    """render the hoem page"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True

    return render_template("index.html", loggedin=login_status)

@app.route('/laptops')
def lt_page():
    """make the laptop page"""
    respons = requests.get('http://127.0.0.1:5000/api/v1/products/laptops')
    laptops = respons.json()
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    return render_template('laptops.html', laptops=laptops, loggedin=login_status)

@app.route('/apple')
def apple():
    """the apple home page"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    return render_template('apple.html', loggedin=login_status)

@app.route('/apple/apple_lt')
def apple_lt():
    """ the macbooks page"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    data = requests.get('http://127.0.0.1:5000/api/v1/products/apple/laptop').json()
    return render_template('apple-lt.html', laptops=data, loggedin=login_status)

@app.route('/apple/apple_dt')
def apple_dt():
    """ the macbooks page"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    data = requests.get('http://127.0.0.1:5000/api/v1/products/apple/desktop').json()
    return render_template('apple-dt.html', desktops=data, loggedin=login_status)

@app.route('/accessories')
def accessory():
    """the accessories main patge"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    data = requests.get('http://127.0.0.1:5000/api/v1/products/accessories').json()
    return render_template("acc.html", accs=data, loggedin=login_status)

@app.route('/your_shopping_cart')
def shopping_cart():
    """defining shopping cart page"""
    login_status = False
    if current_user.is_authenticated:
        login_status = True
    
    session_cookie = request.cookies.get('session')  # Get the session cookie
    total_price = 0

    # Pass the session cookie to the request headers
    response = requests.get('http://127.0.0.1:5000/api/v1/shopping_cart_to_show', cookies={'session': session_cookie})

    if response.status_code == 401:
        response = requests.get('http://127.0.0.1:5000/api/v1/loggout_shopping_cart_to_show')
    
    data = response.json()

    for el in data.values():
        total_price += el[0]['price'] * len(el)
    
    return render_template('shopping_cart.html', elements=data, total_price=round(total_price, 2), loggedin=login_status)


