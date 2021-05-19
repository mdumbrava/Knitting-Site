from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def main():
   value = "About Us"
   return render_template('about.html', value=value,)