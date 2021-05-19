from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def shop():
   value = "Shop Catalog"
   return render_template('policy.html', value=value,)

@bp.route('/hats')
def hats():
   value = "Shipping Info"
   return render_template('policy.html', value=value,)