import requests
from flask import (
    Blueprint, session
)

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    reponse = requests.get('http://user-service:8001/auth/register')
    return reponse.content

@bp.route('/login', methods=('GET', 'POST'))
def login():
    response = requests.get('http://user-service:8001/auth/login')
    return response.content

@bp.route('/logout')
def logout():
    response = requests.get('http://user-service:8001/auth/logout')
    return response.content