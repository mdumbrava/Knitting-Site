""" This package handles privacy policy Page app """
from flask import Blueprint

bp = Blueprint('policy', __name__, url_prefix='/policy')

from . import routes