from flask import render_template, redirect, request, session
from . import bp
from datetime import date
from knit.db_knit import TblProducts
from knit import db

@bp.route('/')
def shop():
   value = "Shop Catalog"
   return render_template('/shop/shop.html', value=value,)

@bp.route('/hats')
def hats():
   value = "Shop Hats"
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter_by(category="hat").all()
   db.session.close()
   return render_template('shop/hats.html', value=value, data=data)

@bp.route('/gloves')
def gloves():
   value = "Shop gloves"
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter_by(category="gloves").all()
   db.session.close()
   return render_template('shop/gloves.html', value=value, data=data)

@bp.route('/sweaters')
def sweaters():
   value = "Shop Sweaters"
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter_by(category="sweaters").all()
   db.session.close()
   return render_template('shop/sweaters.html', value=value, data=data)

@bp.route('/blankets')
def blankets():
   value = "Shop Blankets"
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter_by(category="blankets").all()
   db.session.close()
   return render_template('shop/blankets.html', value=value, data=data)

@bp.route('/scarves')
def scarves():
   value = "Shop Scarves"
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter_by(category="scarves").all()
   db.session.close()
   return render_template('shop/scarves.html', value=value, data=data)

# this is for the search option 
@bp.route('/search_form')
def search_form():
   value = "Search"
   return render_template('shop/search_form.html', value=value,)

@bp.route('/search' , methods=["POST"])
def search():
   value = "Search Results"
   val_search=request.form ["search"]
   data=TblProducts.query.order_by(TblProducts.id.desc()).filter(
      (TblProducts.name.like('%{}%'.format(val_search))) | 
      (TblProducts.desc.like('%{}%'.format(val_search))) | 
      (TblProducts.category.like('%{}%'.format(val_search)))  
      ).all()
   db.session.close()
   return render_template('shop/search.html', value=value, data=data)