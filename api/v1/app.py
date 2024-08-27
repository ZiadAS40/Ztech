#!/usr/bin/python3
""" Flask Application """

from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS



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
