#!/usr/bin/python3
"""make the laptops section"""

from api.v1.views import app_views
import uuid
from flask import jsonify, make_response, request, abort

orders = {}
def remove_duplicates(d):
    seen_values = []
    result = {}
    for key, value in d.items():
        if value not in seen_values:
            result[key] = value
            seen_values.append(value)
    return result

@app_views.route('/shopping_cart', methods=['GET'], strict_slashes=False)
def shopping_getter():
    """make the api for getting the orders"""
    return make_response(jsonify(orders), 200)

@app_views.route('/shopping_cart_to_show', methods=['GET'], strict_slashes=False)
def shopping_getter_to_show():
    """make the api for getting the orders"""
    elements = {obje['id']: [obj for obj in orders.values() if obj['id'] == obje['id']] for obje in orders.values()}
    uniqueEls = remove_duplicates(elements)
    return make_response(jsonify(uniqueEls), 200)

@app_views.route('/shopping_cart', methods=['POST'], strict_slashes=False)
def shopping_setter():
    """setting the order"""
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

    return make_response(jsonify(data), 201)

@app_views.route('/shopping_cart/<order_id>', methods=['DELETE'], strict_slashes=False)
def shopping_del(order_id):
    """deleting the order for dynamic show"""
    if order_id not in orders:
        abort(404, description="Order not found")

    del orders[order_id]

    return make_response(jsonify({}), 200)
