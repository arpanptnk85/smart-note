from bson import ObjectId
from datetime import datetime
from typing import Any
from mongoengine.queryset import QuerySet

def serialize_document(doc: Any):
    """
    Convert mongoengine document to a JSON-Serializable dictionary.
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