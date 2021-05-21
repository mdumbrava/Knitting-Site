""" This package handles shop Page app """
from flask import Blueprint

bp = Blueprint('shop', __name__, url_prefix='/shop')

from . import routes