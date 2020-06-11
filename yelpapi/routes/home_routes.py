from flask import jsonify, Blueprint


home_routes = Blueprint("home_routes", __name__)


@home_routes.route('/')
def test_app():
    version = "0.1"
    return f"YELP DATASET REST API is working version {version}"


@home_routes.route('/hello')
def hello():
    return "HELLO!"