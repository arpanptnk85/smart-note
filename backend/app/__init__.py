import os
from flask import Flask
from dotenv import load_dotenv
from .routes.auth_routes import auth_bp
from .routes.user_routes import user_bp
from .routes.note_routes import note_bp
from flask_jwt_extended import JWTManager

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the Database 
    from . import database
    database.connect_db()

    # Set the secret key for JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')  # Change this in production
    
    # Specify where the JWT should be looked for (headers by default)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Could also be 'cookies', 'query_string', 'json'

    # Initialize JWT Manager
    jwt = JWTManager(app)

    # Register blueprint for routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(note_bp)
    
    return app