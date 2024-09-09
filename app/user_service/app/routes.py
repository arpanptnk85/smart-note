from flask import ( Blueprint, jsonify, request )
from app.utils import serialize_document
from app.crud import ( create_user, update_user, delete_user, get_user_by_id )

user_bp = Blueprint('user', __name__, url_prefix='/auth')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        user = create_user(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        serialized_data = serialize_document(user)
        return jsonify(serialized_data)
    return jsonify({'message': 'UnAuthorized Access Denied'}, 404)

@user_bp.route('/users/<user_id>', methods=['GET'])
def fetch_user_by_id(user_id):
    user = get_user_by_id(user_id=user_id)
    serialized_data = serialize_document(user)
    return jsonify(serialized_data)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify({'message': 'User login', 'token': 'aa2r3v3cq'}, 200)

@user_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'User Logout'}, 200)
