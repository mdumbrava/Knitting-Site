from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from config import KEY, SQL


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)

    # flask admin config

    from knit.db_knit import TblUsers

    from knit.db_knit import TblProducts


    def check_admin():
        try:
            user = session["USER_ID"]
            print (user)
            if user == "miha_123@gmail.com":
                return True
        except:
            return False


    # this will allow tables
    class MyModelView(ModelView):
        page_size    = 1000
        can_view_details = True
        column_exclude_list = ['passwd', ]
        def is_accessible(self):
            return check_admin()

    class MyAdminView(AdminIndexView):
        def is_accessible(self):
            return check_admin()

    admin = Admin(app, index_view=MyAdminView(), template_mode='bootstrap4', name='WebTools')
    admin.add_view(MyModelView    (TblUsers,  db.session))
    admin.add_view(MyModelView    (TblProducts,  db.session))



    # home BP
    from knit.home import bp as home
    app.register_blueprint(home)

    # # My Account Blueprint
    from knit.account import bp as account
    app.register_blueprint(account)

    # # # about us Blueprint
    from knit.about import bp as about
    app.register_blueprint(about)
    
    # # # privacy policy Blueprint
    from knit.policy import bp as policy
    app.register_blueprint(policy)
 
    # # # customer service Blueprint
    from knit.service import bp as service
    app.register_blueprint(service)
    
    # # # shop Blueprint
    from knit.shop import bp as shop
    app.register_blueprint(shop)

    #     # Authenticate Blueprint
    # from KDA.Auth import bp as Auth
    # app.register_blueprint(Auth)

    return app