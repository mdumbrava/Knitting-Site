""" This package handles customer service Page app """
from flask import Blueprint

bp = Blueprint('service', __name__, url_prefix='/service')

from . import routes