"""Main application and routing logic for Yelp API."""
from decouple import config
from flask import Flask
from yelpapi.routes.home_routes import home_routes



def create_app():
    """Application Factory Pattern"""
    """Create and configure and instance of flask application."""
    app = Flask(__name__)
    CORS(app) # Flask CORS, https://flask-cors.readthedocs.io/en/latest/

    # Registering routes
    app.register_blueprint(home_routes)
    
    

    return app