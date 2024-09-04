#!/user/bin/python3
""" the main app routes """


from flask import Flask, make_response, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

def configure_app():
    from api.v1.views import app_views
    app.register_blueprint(app_views, url_prefix='/api/v1')


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/')
def homePage():
    """render the hoem page"""
    return render_template("index.html")

@app.route('/laptops')
def lt_page():
    """make the laptop page"""
    respons = requests.get('http://127.0.0.1:5000/api/v1/products/laptops')
    laptops = respons.json()
    return render_template('laptops.html', laptops=laptops)

@app.route('/apple')
def apple():
    """the apple home page"""
    return render_template('apple.html')

@app.route('/apple/apple_lt')
def apple_lt():
    """ the macbooks page"""
    data = requests.get('http://127.0.0.1:5000/api/v1/products/apple/laptop').json()
    return render_template('apple-lt.html', laptops=data)

@app.route('/apple/apple_dt')
def apple_dt():
    """ the macbooks page"""
    data = requests.get('http://127.0.0.1:5000/api/v1/products/apple/desktop').json()
    return render_template('apple-dt.html', desktops=data)

@app.route('/accessories')
def accessory():
    """the accessories main patge"""
    data = requests.get('http://127.0.0.1:5000/api/v1/products/accessories').json()
    return render_template("acc.html", accs=data)

@app.route('/your_shopping_cart')
def shopping_cart():
    """defining shopping cart page"""
    data = requests.get('http://127.0.0.1:5000/api/v1/shopping_cart_to_show').json()
    total_price = 0
    for el in data.values():
        total_price += el[0]['price'] * len(el)
    return render_template('shopping_cart.html', elements=data, total_price=round(total_price, 2))
