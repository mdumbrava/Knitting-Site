from flask import render_template, redirect, request, session
from . import bp
from datetime import date

@bp.route('/')
def main():
   value = "My Account"
   return render_template('account.html', value=value,)

@bp.route('/login')
def login():
   value = "Login Page"
   return render_template('login.html', value=value,)

@bp.route('/register')
def register():
   value = "Register Page"
   return render_template('register.html', value=value,)