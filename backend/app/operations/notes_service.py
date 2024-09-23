from app.models import Notes
from typing import Any, List

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