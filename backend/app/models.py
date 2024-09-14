from mongoengine import ( Document, StringField, DateTimeField, ReferenceField, ListField )
from datetime import datetime, timezone
from app.utils import get_current_time

# User Model
class Users(Document):
    username = StringField(required=True, max_length=50, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=get_current_time())
    updated_at = DateTimeField(default=get_current_time())

    # Meta to specifiy collection and indexes
    meta = {
        'collection': 'users',
        'ordering': ['-created_at'],
        'indexes': ['email']
    }

    def save(self, *args, **kwargs):
        self.updated_at = get_current_time()
        return super(Users, self).save(*args, **kwargs)
    
# Notes Model
class Notes(Document):
    user_id = ReferenceField(Users)
    title = StringField(required=True, max_length=100)
    text = StringField(required=True)
    tag = ListField(StringField())
    depth = StringField(default='normal')
    created_at = DateTimeField(default=get_current_time())
    updated_at = DateTimeField(default=get_current_time())

    # Meta to specifiy collection and indexes
    meta = {
        'collection': 'notes',
        'ordering': ['-created_at'],
        'indexes': ['user_id']
    }

    def save(self, *args, **kwargs):
        self.updated_at = get_current_time()
        return super(Notes, self).save(*args, **kwargs)