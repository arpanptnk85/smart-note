import os
import jwt
from flask import jsonify
from app.models import User
from typing import Dict, Any
from datetime import timedelta, datetime, timezone
from app.utils import serialize_document
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
    # Generate the jwt encoded token
    # payload = {
    #     'sub': user_id,
    #     'iat': datetime.now(timezone.utc),
    #     'exp': datetime.now(timezone.utc) + timedelta(hours=1),
    #     'type': 'access',
    # }
    # token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    token = create_access_token(identity=user_id, expires_delta=timedelta(hours=1))
    return token

def validate_access_token(jwt_token: str):
    payload = jwt.decode(jwt=jwt_token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def login_user(username: str, password: str) -> Any:
    _user = User.objects(username=username).first()
    if not _user:
        return jsonify({'message': 'Invalid username'}), 401
    
    user = serialize_document(_user)
    if user.get('password') != password:
        return jsonify({'message': 'Invalid username or password'}), 401
    access_token = generate_access_token(user_id=user.get('_id'))
    return jsonify(access_token=access_token), 200
