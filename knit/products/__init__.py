""" This package handles admin adding products Page app """
from flask import Blueprint

bp = Blueprint('products', __name__, url_prefix='/products')

from . import routes