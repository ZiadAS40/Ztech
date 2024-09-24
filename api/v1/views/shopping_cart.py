#!/usr/bin/python3
"""make the laptops section"""

from api.v1.views import app_views
import json
from flask import jsonify, make_response, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_login import login_required, current_user

orders = {}



def remove_duplicates(d):
    seen_values = []
    result = {}
    for key, value in d.items():
        if value not in seen_values:
            result[key] = value
            seen_values.append(value)
    return result

# get the cart for ths user (get the count)
@app_views.route('/shopping_cart', methods=['GET'], strict_slashes=False)
@login_required
def shopping_getter():
    """make the api for getting the orders"""
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}
    
    try:
        return make_response(jsonify(users_orders[current_user.id]), 200)
    except KeyError:
        return make_response(jsonify({}), 201)
    

# get the cart for ths user (get the count)
@app_views.route('/loggout_shopping_cart', methods=['GET'], strict_slashes=False)
def shopping_loggout_getter():
    """make the api for getting the orders"""
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}
    try:
        return make_response(jsonify(users_orders['unknowen']), 200)
    except KeyError:
        return make_response(jsonify({}), 201)        

# get the cart for the user to show in the shopping cart page
@app_views.route('/shopping_cart_to_show', methods=['GET'], strict_slashes=False)
@login_required
def shopping_getter_to_show():
    """make the api for getting the orders"""
    # making a special dict {'object's is': [list of all the abjects with the same id]}

    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}
    
    return make_response(jsonify(users_orders[current_user.id]), 200)


# get the cart for the user to show in the shopping cart page (loggout)
@app_views.route('/loggout_shopping_cart_to_show', methods=['GET'], strict_slashes=False)
def loggout_getter_to_show():
    """Handle the logout data to show"""
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}    
    
    return make_response(jsonify(users_orders['unknowen']), 200)


@app_views.route('/shopping_cart', methods=['POST'], strict_slashes=False)
@jwt_required()
def shopping_setter():
    """setting the order"""
    user_id = get_jwt_identity()
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}

    if not request.get_json():
        abort(400, description="Missing JSON data")

    data = request.get_json()
    
    if 'id' not in data:
        abort(400, description="Missing 'id' in request data")
    
    
    order_id = data['id']

    if user_id not in users_orders:
        users_orders[user_id] = {}
    
    if user_id in users_orders and order_id not in users_orders[user_id]:
        users_orders[user_id][order_id] = []

    users_orders[user_id][order_id].append(data)   
    
    with open('users.json', 'w') as f:
        json.dump(users_orders, f)

    return make_response(jsonify(data), 201)

# making the loggout user cart
@app_views.route('/loggout_shopping_cart', methods=['POST'], strict_slashes=False)
def loggout_cart():
    """making the loggout shopping cart"""
    if not request.get_json():
        abort(400, description="Missing JSON data")
    
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}

    user_id = 'unknowen'
    data = request.get_json()
    
    if 'id' not in data:
        abort(400, description="Missing 'id' in request data")
    
    
    order_id = data['id']

    if user_id not in users_orders:
        users_orders[user_id] = {}
    
    if user_id in users_orders and order_id not in users_orders[user_id]:
        users_orders[user_id][order_id] = []

    users_orders[user_id][order_id].append(data)

    with open('users.json', 'w') as f:
        json.dump(users_orders, f)

    return make_response(jsonify(data), 201)

    



@app_views.route('/shopping_cart/<order_id>', methods=['DELETE'], strict_slashes=False)
def shopping_del(order_id):
    """deleting the order for dynamic show"""
    if order_id not in orders:
        abort(404, description="Order not found")

    del orders[order_id]

    return make_response(jsonify({}), 200)


@app_views.route('/sync', methods=['POST'], strict_slashes=False)
@login_required
def sync_loggout_with_user():
    """
    making syncronizatoin between the shopping cart for a user
    and the loggout shopping cart
    """
    try:
        with open('users.json', 'r') as f:
            if f.read().strip() == "":
                users_orders = {}
            else:
                f.seek(0)
                users_orders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users_orders = {}
    for order, value in users_orders.items():
        if order not in users_orders[current_user.id]:
            users_orders[current_user.id][order] = value
        del loggout_cart[order]
    
    return make_response(jsonify(users_orders[current_user.id]), 201)

