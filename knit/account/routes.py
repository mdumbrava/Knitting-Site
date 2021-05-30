from flask import render_template, redirect, request, session
from . import bp
from datetime import date
from knit.db_knit import TblUsers
from knit import db
from werkzeug.security import check_password_hash, generate_password_hash
from knit.user import getuser


@bp.route('/')
def main():
   email=getuser()
   value = "My Account"
   return render_template('account.html', value=value, email=email,)

@bp.route('/loginform')
def loginform():
   value = "Login Page"
   return render_template('login.html', value=value,)

@bp.route('/form')
def form():
   value = "Register Page"
   return render_template('register.html', value=value,)

@bp.route('/login', methods=["POST"])
def login():
    print(request.form["email"])
    print(request.form["password"])
    data=TblUsers.query.filter_by(email=request.form["email"]).first()
    if data:
        print("email exists")
        if check_password_hash(data.password, request.form['password']):
            print("pass ok")
            session["USER_ID"] = request.form['email']
            return redirect ("/")
    else:
        print("user doesnt exist")
    return redirect ("/loginform")

@bp.route('/register', methods=["POST"])
def register():
    print(request.form["email"])
    print(request.form["password"])
    check=TblUsers.query.filter_by(email=request.form["email"]).first()
    if request.form["password"] != request.form["password1"]:
        return "passwords do not match"
    if not check:
        data=TblUsers(email=request.form["email"], password=generate_password_hash(request.form["password"], "sha256"))
        db.session.add(data)
        db.session.commit()
        db.session.close()
        session["USER_ID"] = request.form['email']
        return redirect ("/")
    else:
        return "Username already exists"

@bp.route('/logout')
def logout():
    session.pop("USER_ID", None)
    return redirect ("/")