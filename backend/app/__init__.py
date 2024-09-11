import os
from flask import Flask
from dotenv import load_dotenv
from .routes import usernotes_bp
from flask_jwt_extended import JWTManager

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE_URI='mongodb://localhost:27017/smart-note',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Database 
    from . import database
    database.connect_db()

    # JWT
    # Set the secret key for JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')  # Change this in production
    
    # Specify where the JWT should be looked for (headers by default)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Could also be 'cookies', 'query_string', 'json'

    # Initialize JWT Manager
    jwt = JWTManager(app)

    # Routes
    app.register_blueprint(usernotes_bp)
    
    return app