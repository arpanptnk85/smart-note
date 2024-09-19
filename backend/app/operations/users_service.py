import logging
from app.models import Users
from typing import Any, Dict
from app.utils import DuplicateItemError
from werkzeug.security import generate_password_hash
from mongoengine.errors import DoesNotExist, ValidationError, NotUniqueError

# Setup logging
logger = logging.getLogger(__name__)

def get_user_info(user: Users) -> Dict[str, Any]:

    if not user:
        logger.error(f'User does not exists.')
        return {}

    try:
        return {
            'id': str(user.id),
            'email': user.email,
            'username': user.username
        }
    except Exception as e:
        logger.error(f'Unexpected error occurred at `get_user_info`: {e}')
        return {}

# Create an user
def create_user(username: str, password: str, email: str) -> Any:
    """ Create a new user """
    
    if not username or not password or not email:
        raise ValueError('Username, password or email are required.')
    
    try:

        if Users.objects(username=username).first():
            raise DuplicateItemError('username', username)
        
        if Users.objects(email=email).first():
            raise DuplicateItemError('email', email)
        
        # Hashed password
        _password = generate_password_hash(password)

        user = Users(username=username, email=email, password=_password)
        user.save()

        return get_user_info(user=user)
    
    except NotUniqueError as e:
        print(f"Duplicate entry {e}")
        raise DuplicateItemError('username or email', f'{username} / {email}')
    
    except ValidationError as e:
        print(f"Validation error while creating user: {e}")
        raise ValueError(f"Invalid data: {e}")
    
    except Exception as e:
        print(f"Unexpected error while creating user: {e}")
        raise Exception('An error occurred while creating the user')

# Get user by _id
def get_user_by_id(user_id):
    try:
        user = Users.objects(id=user_id).first()
        return get_user_info(user=user)
    except DoesNotExist:
        logger.error(f'User with ID {user_id} does not exists.')
        return {}

# Get user by email
def get_user_by_email(email):
    try:
        user = Users.objects(email=email).first()
        return get_user_info(user=user)
    except DoesNotExist:
        logger.error(f'User with email {email} does not exists.')

# Get all users
def get_users(limit: int = 100):
    users = Users.objects.limit(limit).only('username', 'email', 'id')
    return [get_user_info(user=u) for u in users]
    
# Update an user
def update_user(user_id, **kwargs):
    try:
        user = Users.objects(id=user_id).first()
        for key, value in kwargs.items():
            if key == 'password': # Hash the password
                value = generate_password_hash(value)
            setattr(user, key, value)
        user.save()
        return get_user_info(user=user)
    
    except ValidationError as e:
        logger.error(f'Validation error while updating user: {e}')
        raise ValueError(f'Invalid data: {e}')
    
    except DoesNotExist:
        logger.error(f'User with ID: {user_id} does not exists')
        return None

# Delete an user
def delete_user(user_id):
    try:
        user = Users.objects(id=user_id).first()
        user.delete()
        return True
    except DoesNotExist:
        logger.error(f'User with ID {user_id} does not exists.')
        raise ValueError('User not found')

# Validate user
def validate_user(user_id: str) -> bool:
    """ User verification """
    try:
        Users.objects.only('id').get(id=user_id)
        return True
    except (DoesNotExist, ValidationError) as e:
        print(f'User validation failed: {e}')
        return False
    except Exception as e:
        print(f'Unexpected error occurred during user validation: {e}')
        return False