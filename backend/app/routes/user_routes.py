from flask import ( Blueprint, jsonify )
from app.utils import serialize_document
from flask_jwt_extended import jwt_required
from app.operations.users_service import ( get_users, get_user_by_id )

user_bp = Blueprint('user', __name__)

@user_bp.route('v1/users/<user_id>', methods=['GET'])
@jwt_required()
def fetch_user_by_id(user_id):
    if user_id is None:
        return jsonify({'message': 'Not Found'})
    try:
        user = get_user_by_id(user_id=user_id)
        serialized_data = serialize_document(user)
        return jsonify(serialized_data), 200
    except Exception as e:
        print(f'Error fetching user {e}')
        return jsonify({'error': e}), 422

@user_bp.route('v1/users', methods=['GET'])
@jwt_required()
def fetch_users():
    try:
        user = get_users()
        serialized_data = serialize_document(user)
        return jsonify(serialized_data), 200
    except Exception as e:
        print(f'Error fetching user {e}')
        return jsonify({'error': e}), 422