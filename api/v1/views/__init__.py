#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)


from api.v1.views.laptop import *
from api.v1.views.acc import *
from api.v1.views.apple_dt import *
from api.v1.views.apple_lt import *
from app.routes import *