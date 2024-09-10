from flask import ( Blueprint, jsonify, request )
from app.utils import serialize_document
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
        return jsonify({'token': 'aa2r3v3cq'}), 200

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