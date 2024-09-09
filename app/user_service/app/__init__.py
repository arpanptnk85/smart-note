from flask import Flask
from . import routes

app = Flask(__name__)
app.register_blueprint(routes.user_bp)