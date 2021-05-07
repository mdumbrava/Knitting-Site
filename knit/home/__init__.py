""" This package handles home Page app """
from flask import Blueprint

bp = Blueprint('home', __name__, url_prefix='/')

from . import routes