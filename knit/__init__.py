from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import KEY, SQL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)



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