from flask import (
    Blueprint, jsonify
)

user_bp = Blueprint('user', __name__, url_prefix='/auth')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    return jsonify({'message': 'User registered', 'token': 'aa2r3v3cq'}, 201)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify({'message': 'User login', 'token': 'aa2r3v3cq'}, 200)

@user_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'User Logout'}, 200)
