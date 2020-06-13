"""The main application and routing logic for Yelp Flask API"""

from decouple import config
from flask import Flask
from flask_cors import CORS
from yelpapi.routes.home_routes import home_routes

def create_app():
    """Application Factory Pattern"""
    """Create, Configure, and Instance of Flask App"""
    app = Flask(__name__)
    CORS(app) #Flask CORS, https://flask-cors.readthedocs.io/en/latest/

    # Registering routes
    app.register_blueprint(home_routes)
    return app



