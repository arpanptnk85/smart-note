from app.auth import login_user
from app.utils import DuplicateItemError
from flask import ( Blueprint, jsonify, request, session )
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.operations.users_service import ( create_user )

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    _username = data.get('username')
    _password = data.get('password')
    _email = data.get('email')

    if not _username or not _password or not _email:
        return jsonify({ 'message': 'Missing required fields' }), 400

    try:
        user = create_user(username=_username, password=_password, email=_email)
        return jsonify({ 'message': 'success' }), 201
    except DuplicateItemError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'An unexpected error occurred'}), 500
    

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        username = data.get('username')
        password = data.get('password')
        return login_user(username, password)
    except Exception as e:
        return jsonify({'message': 'An unexpected error occurred'}), 500

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    session.clear()
    return jsonify({'message': 'User Logged out'}), 200

@auth_bp.route('/token-verify', methods=['POST'])
@jwt_required()
def verify_token():
    user_id = get_jwt_identity()
    return jsonify({'message': 'Token is valid', 'user_id': user_id}), 200