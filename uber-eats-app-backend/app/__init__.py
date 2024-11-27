from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.routes.auth_routes import auth_routes
from app.routes.menu_routes import menu_routes
from app.routes.order_routes import order_routes
from app.routes.payment_routes import payment_routes
from app.routes.restaurant_routes import restaurant_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uber_eats.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "supersecretkey"

    db.init_app(app)
    CORS(app)

    # Login routes
    app.register_blueprint(auth_routes, url_prefix='/auth')
    app.register_blueprint(menu_routes, url_prefix='/api/menu')
    app.register_blueprint(order_routes, url_prefix='/api')
    app.register_blueprint(payment_routes, url_prefix='/api')
    app.register_blueprint(restaurant_routes, url_prefix='/api/restaurants')


    return app
