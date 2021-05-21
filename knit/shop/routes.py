from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def shop():
   value = "Shop Catalog"
   return render_template('/shop/shop.html', value=value,)

@bp.route('/hats')
def hats():
   value = "Shop Hats"
   return render_template('shop/hats.html', value=value,)

@bp.route('/gloves')
def gloves():
   value = "Shop gloves"
   return render_template('shop/gloves.html', value=value,)

@bp.route('/sweaters')
def sweaters():
   value = "Shop Sweaters"
   return render_template('shop/sweaters.html', value=value,)

@bp.route('/blankets')
def blankets():
   value = "Shop Blankets"
   return render_template('shop/blankets.html', value=value,)

@bp.route('/scarves')
def scarves():
   value = "Shop Scarves"
   return render_template('shop/scarves.html', value=value,)