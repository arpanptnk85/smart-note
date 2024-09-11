import jwt
from app.auth import login_user, validate_access_token
from app.utils import serialize_document
from flask import ( Blueprint, jsonify, request )
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.crud import ( create_user, get_users, get_user_by_id )

usernotes_bp = Blueprint('usernotes', __name__)

@usernotes_bp.route('/auth/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        user = create_user(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        serialized_data = serialize_document(user)
        return jsonify(serialized_data)
    return jsonify({'message': 'UnAuthorized Access Denied'}), 404

@usernotes_bp.route('/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return login_user(username, password)

@usernotes_bp.route('/auth/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'User Logout'}), 200

@usernotes_bp.route('/users/<user_id>', methods=['GET'])
def fetch_user_by_id(user_id):
    if user_id is None:
        return jsonify({'message': 'Not Found'})
    try:
        user = get_user_by_id(user_id=user_id)
        serialized_data = serialize_document(user)
        return jsonify(serialized_data), 200
    except Exception as e:
        print(f'Error fetching user {e}')

@usernotes_bp.route('/users', methods=['GET'])
def fetch_users():
    try:
        user = get_users()
        serialized_data = serialize_document(user)
        return jsonify(serialized_data), 200
    except Exception as e:
        print(f'Error fetching user {e}')

@usernotes_bp.route('/auth/token-verify', methods=['POST'])
@jwt_required()
def verify_token():
    user_id = get_jwt_identity()
    return jsonify({'message': 'Token is valid', 'user_id': user_id}), 200