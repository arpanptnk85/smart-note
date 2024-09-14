from uuid import uuid4
from bson import ObjectId
from typing import Any, Dict
from datetime import datetime, timezone
from mongoengine.queryset import QuerySet

def generate_hex_code(length: int = 6):
    return str(uuid4().hex[:length])

def get_current_time() -> datetime:
    """
    Generates the current time in UTC timezone.

    Returns
        A datetime object
    """
    return datetime.now(timezone.utc)

def serialize_document(doc: Any) -> Dict:
    """
    Convert mongoengine document to a JSON-Serializable dictionary.

    Args
        doc: A Object of type Document.

    Returns:
        Dict 
    """
    def serialize(value: Any):

        if isinstance(value, ObjectId):
            return str(value)
        elif isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, dict):
            return {k: serialize(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [serialize(item) for item in value]
        else:
            return value
        
    if doc is None: return None

    if isinstance(doc, QuerySet):
        return [serialize(d.to_mongo().to_dict()) for d in doc]
    else:
        return serialize(doc.to_mongo().to_dict())
    
class DuplicateItemError(Exception):
    """Exception raised when an item is already present in a collection."""

    def __init__(self, item_name: str, item_value: str):
        """Initialize the exception with the duplicate item."""
        super().__init__(f"{item_name.capitalize()} '{item_value}' already exists.")