from app.models import Notes
from typing import Any, List
from app.utils import serialize_document

# Create a Note
def add_note(user_id: Any, title: str, text: str, tags: List[str], depth: str) -> Any:
    """Creates a new note"""
    note = Notes(
        user_id=user_id,
        title=title,
        text=text,
        tag=tags,
        depth=depth
    )
    note.save()
    return note

# Filter notes by user
def get_notes_by_user(user_id: str, limit: int = 100) -> Any:
    """
    Filters the notes by user and returns
    
    Args
        user_id str: A user _id.
        limit  int: limits query to limit.

    Returns
        List of filtered notes.
    """

    if not user_id:
        raise ValueError("User id not valid.")

    _notes = Notes.objects(user_id=user_id).limit(limit)
    filtered_notes = [serialize_document(note) for note in _notes]
    return filtered_notes