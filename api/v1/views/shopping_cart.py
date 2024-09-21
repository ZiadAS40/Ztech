#!/usr/bin/python3
"""make the laptops section"""

from api.v1.views import app_views
import uuid
from flask import jsonify, make_response, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import User
from flask_login import login_required, current_user
from app.routes import app

orders = {}
loggout_orders = {}
users_orders = {}
def remove_duplicates(d):
    seen_values = []
    result = {}
    for key, value in d.items():
        if value not in seen_values:
            result[key] = value
            seen_values.append(value)
    return result


@app_views.route('/shopping_cart', methods=['GET'], strict_slashes=False)
@login_required
def shopping_getter():
    """make the api for getting the orders"""
    try:
        return make_response(jsonify(users_orders[current_user.id]), 200)
    except KeyError:
        return make_response(jsonify({}), 201)

@app_views.route('/loggout_shopping_cart', methods=['GET'], strict_slashes=False)
def shopping_loggout_getter():
    """make the api for getting the orders"""
    try:
        return make_response(jsonify(loggout_orders), 200)
    except KeyError:
        return make_response(jsonify({}), 201)        

# making get request after the POST request to fill orders
@app_views.route('/shopping_cart_to_show', methods=['GET'], strict_slashes=False)
@login_required
def shopping_getter_to_show():
    """make the api for getting the orders"""
    # making a special dict {'object's is': [list of all the abjects with the same id]}
    current_id = current_user.id
    if current_id in users_orders:    

        elements = {obje['id']: [obj for obj in users_orders[current_id].values() if obj['id'] == obje['id']] for obje in users_orders[current_id].values()}

        uniqueEls = remove_duplicates(elements)

        return make_response(jsonify(uniqueEls), 200)
    else:
        return make_response(jsonify({}), 404)

# Making GET request for the logout to show
@app_views.route('/loggout_shopping_cart_to_show', methods=['GET'], strict_slashes=False)
def loggout_getter_to_show():
    """Handle the logout data to show"""
    elements = {obj['id']: [obje for obje in loggout_orders.values() if obj['id'] == obje['id']] for obj in loggout_orders.values()}
    
    uniqueEls = remove_duplicates(elements)
    
    return make_response(jsonify(uniqueEls), 200)


@app_views.route('/shopping_cart', methods=['POST'], strict_slashes=False)
@jwt_required()
def shopping_setter():
    """setting the order"""
    user_id = get_jwt_identity()

    if not request.get_json():
        abort(400, description="Missing JSON data")

    data = request.get_json()
    
    if 'id' not in data:
        abort(400, description="Missing 'id' in request data")
    
    if data['id'] in orders:
        order_id = str(uuid.uuid4())
    else:
        order_id = data['id']
    orders[order_id] = data
    if user_id not in users_orders:
        users_orders[user_id] = {}

    users_orders[user_id][order_id] = data

    return make_response(jsonify(data), 201)

# making the loggout user cart
@app_views.route('/loggout_shopping_cart', methods=['POST'], strict_slashes=False)
def loggout_cart():
    """making the loggout shopping cart"""
    if not request.get_json():
        abort(400, description="Missing JSON data")

    data = request.get_json()
    
    if 'id' not in data:
        abort(400, description="Missing 'id' in request data")
    
    if data['id'] in loggout_orders:
        order_id = str(uuid.uuid4())
    else:
        order_id = data['id']
    loggout_orders[order_id] = data

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
    for order, value in loggout_orders.items():
        if order not in users_orders[current_user.id]:
            users_orders[current_user.id][order] = value
        del loggout_cart[order]
    
    return make_response(jsonify(users_orders[current_user.id]), 201)

