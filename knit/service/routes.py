from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/contact')
def contact():
   value = "Contact Us"
   return render_template('contact.html', value=value,)

@bp.route('/shipping')
def shipping():
   value = "Shipping Info"
   return render_template('shipping.html', value=value,)