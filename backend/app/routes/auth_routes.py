import jwt
from app.auth import login_user
from app.utils import serialize_document
from flask import ( Blueprint, jsonify, request )
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.operations.users_service import ( create_user )

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        user = create_user(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        serialized_data = serialize_document(user)
        return jsonify(serialized_data)
    return jsonify({'message': 'UnAuthorized Access Denied'}), 404

@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return login_user(username, password)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'User Logout'}), 200

@auth_bp.route('/token-verify', methods=['POST'])
@jwt_required()
def verify_token():
    user_id = get_jwt_identity()
    return jsonify({'message': 'Token is valid', 'user_id': user_id}), 200