#!usr/bin/python3

from api.v1.views import app_views
import json
from flask import jsonify, make_response, request, abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_login import login_required, current_user
from laptops import rate_laps
import re

def get_budget(laps, budget):
    final_laps = []
    
    for lap in laps:
        price_str = lap.get('price', '')
        price_match = re.findall(r'\d+', price_str)
        
        if price_match:
            lap_price = int(''.join(price_match))
            
            if lap_price <= budget:
                final_laps.append(lap)
    
    return final_laps


@app_views.route('/SWEs', methods=['POST'], strict_slashes=False)
def get_rated():
    with open('laptops.json', 'r') as f:
        laps = json.load(f)
    
    data = request.get_json()

    budget = data.get('budget')

    final_laps = rate_laps(get_budget(laps, budget))

    sorted_laptops = sorted(final_laps, key=lambda x: x['rate'], reverse=True)
    

    
    return make_response(jsonify(sorted_laptops), 201)
