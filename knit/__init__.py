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



    # KDA Blueprint
    from knit.home import bp as home
    app.register_blueprint(home)

    # # Ahri Blueprint
    from knit.account import bp as account
    app.register_blueprint(account)

    # # # Akali Blueprint
    # from KDA.Akali import bp as Akali
    # app.register_blueprint(Akali)
    
    # # # Evelyn Blueprint
    # from KDA.Evelyn import bp as Evelyn
    # app.register_blueprint(Evelyn)
 
    # # # Kai'sa Blueprint
    # from KDA.Kaisa import bp as Kaisa
    # app.register_blueprint(Kaisa)
    
    # # # Seraphine Blueprint
    # from KDA.Seraphine import bp as Seraphine
    # app.register_blueprint(Seraphine)

    #     # Authenticate Blueprint
    # from KDA.Auth import bp as Auth
    # app.register_blueprint(Auth)

    return app