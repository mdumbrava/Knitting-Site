from flask import render_template, redirect, request, session
from . import bp
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import Flask, session
from knit.db_knit import TblProducts
from knit import db
from knit.user import getuser


@bp.route('/')
@bp.route('/<page>')
def contact(page=None):
   if page:
      page=int(page)
   else:
      page=1

   value = "Admin Page for Adding Products"
   data=TblProducts.query.order_by(TblProducts.id.desc()).paginate(per_page = 3, page = page)
   return render_template('products.html', value=value, data=data, user=getuser())

@bp.route('/add', methods=['POST'])
def add():
   data=TblProducts(name=request.form['name'], desc=request.form['desc'], price=request.form['price'], category=request.form['category'],
   enable=request.form['enable'], picture=request.form['picture'])
   db.session.add(data)
   db.session.commit()
   db.session.close()
   return redirect("/products")

@bp.route('/form/<id>')
def form(id):
   print (id)
   data=TblProducts.query.filter_by(id=id).first()
   db.session.close()
   return render_template('updateform.html', data=data) 

@bp.route('/update', methods=['POST'])
def update():
   print (request.form['id'])
   data=TblProducts.query.filter_by(id=request.form["id"]).first()
   data.name=request.form["name"]
   data.desc=request.form["desc"]
   data.price=request.form["price"]
   data.category=request.form["category"]
   data.enable=request.form["enable"]
   data.picture=request.form["picture"]
   db.session.commit()
   db.session.close()
   return redirect("/products")

@bp.route('/delete/<id>')
def delete(id):
   data=TblProducts.query.filter_by(id=id).first()
   db.session.delete(data)
   db.session.commit()
   db.session.close()
   return redirect("/products")

