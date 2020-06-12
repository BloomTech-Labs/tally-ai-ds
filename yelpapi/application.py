"""The main application and routing logic for Yelp Flask API"""

from decouple import config
from flask import Flask
from flask_cors import CORS
from routes.home_routes import home_routes

def create_app():
    """Application Factory Pattern"""
    """Create, Configure, and Instance of Flask App"""
    application = Flask(__name__)
    CORS(application) #Flask CORS, https://flask-cors.readthedocs.io/en/latest/

    # Registering routes
    application.register_blueprint(home_routes)

    return application


if __name__ == "__main__":
    application = create_app()
    application.run()