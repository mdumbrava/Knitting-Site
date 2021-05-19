from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def main():
   value = "Privacy Policy"
   return render_template('policy.html', value=value,)