from app.utils import serialize_document
from flask import ( Blueprint, jsonify, request )
from app.operations.notes_service import ( add_note )
from app.operations.users_service import validate_user
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint('note', __name__, url_prefix='/api/v1/notes')

@note_bp.route('/add-note', methods=['POST'])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    
    if not user_id: 
        return jsonify({ 'message': 'Unauthorized Access' }), 401
    
    if not validate_user(user_id): 
        return jsonify({ 'message': 'Unauthorized Access' }), 400
    
    data = request.get_json()

    # Validate required fields
    title = data.get('title')
    text = data.get('text')

    if not title or not text:
        return jsonify({ 'message': 'Missing required fields: title and text' }), 400

    note = add_note(
        user_id=user_id,
        title=title,
        text=text,
        tags=data.get('tags'),
        depth=data.get('depth'),
    )
    serialized_data = serialize_document(note)
    return jsonify({'message': serialized_data}), 201
    


