import os
import jwt
from flask import jsonify
from app.models import Users
from typing import Dict, Any
from datetime import timedelta
from app.utils import serialize_document
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')

def generate_access_token(user_id: Any):
    """
    Generates a JWT token with user information and expiration time.

    Args
        user_id: Takes user_id as input.

    Returns
        Encoded JWT Token.
    """
    token = create_access_token(identity=user_id, expires_delta=timedelta(hours=1))
    return token

def validate_access_token(jwt_token: str):
    """
    Validates a proivded JWT Token.
    
    Args
        jwt_token: A JWT Token to be passed as argument.
    
    Returns
        payload
    """
    payload = jwt.decode(jwt=jwt_token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def login_user(username: str, password: str) -> Any:
    _user = Users.objects(username=username).first()

    if not _user:
        return jsonify({'message': 'Invalid username or password'}), 401

    if not check_password_hash(_user.password, password):
        return jsonify({ 'message': 'Invalid username or password' })

    try:
        access_token = generate_access_token(user_id=str(_user.id))
        if not access_token:
            raise ValueError('Failed to generate access token at login')

        user_data = {
            'id': str(_user.id),
            'email': _user.email,
            'username': _user.username
        }

        return jsonify({
            'user': user_data,
            'token': access_token,
        }), 200
    except Exception as e:
        print(f'Error `login` {e}')
        return jsonify({ 'message': 'Unexpected error occurred while `login`' }), 500
