from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def main():
   value = "Welcomes to the Home Page of Miha's knitted goods"
   return render_template('home.html', value=value,)