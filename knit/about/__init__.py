""" This package handles about us Page app """
from flask import Blueprint

bp = Blueprint('about', __name__, url_prefix='/about')

from . import routes