import jwt
from app.auth import login_user, generate_access_token
from app.utils import serialize_document, DuplicateItemError
from flask import ( Blueprint, jsonify, request )
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.operations.users_service import ( create_user )

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = create_user(username=data.get('username'), password=data.get('password'), email=data.get('email'))
<<<<<<< Updated upstream
        return jsonify({ 'message': 'success' }), 201
=======
        serialized_data = serialize_document(user)
        access_token = generate_access_token(user_id=user.get('_id'))
        return jsonify({ 'user': serialized_data, 'token': access_token }), 201
>>>>>>> Stashed changes
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
def logout():
    return jsonify({'message': 'User Logout'}), 200

@auth_bp.route('/token-verify', methods=['POST'])
@jwt_required()
def verify_token():
    user_id = get_jwt_identity()
    return jsonify({'message': 'Token is valid', 'user_id': user_id}), 200