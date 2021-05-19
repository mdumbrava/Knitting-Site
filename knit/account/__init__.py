""" This package handles account Page app """
from flask import Blueprint

bp = Blueprint('account', __name__, url_prefix='/account')

from . import routes