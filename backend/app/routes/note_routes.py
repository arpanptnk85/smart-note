from flask import ( Blueprint, jsonify, request )
from app.utils import serialize_document, generate_hex_code
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.operations.notes_service import ( add_note )

note_bp = Blueprint('note', __name__, url_prefix='/notes')

@note_bp.route('/add-note', methods=['POST'])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    if not user_id: return jsonify({
        'message': 'Unauthorized Access'
    }), 400
    data = request.get_json()
    note = add_note(
        user_id=user_id,
        title=data.get('title'),
        text=data.get('text'),
        tags=data.get('tags'),
        depth=data.get('depth'),
    )
    serialized_data = serialize_document(note)
    return jsonify({'message': serialized_data}), 201
    


