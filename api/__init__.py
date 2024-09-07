from flask import Flask
from . import gateway

app = Flask(__name__) # Register the app

app.register_blueprint(gateway.bp)