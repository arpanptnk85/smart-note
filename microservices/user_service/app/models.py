from mongoengine import ( Document, StringField, DateTimeField )
from datetime import datetime, timezone

# User Model
class User(Document):
    username = StringField(required=True, max_length=50)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    # Meta to specifiy collection and indexes
    meta = {
        'collection': 'users',
        'ordering': ['-created_at'],
        'indexes': ['email']
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(User, self).save(*args, **kwargs)