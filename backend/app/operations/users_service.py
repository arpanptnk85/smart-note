from app.models import Users
from typing import Any, Dict
from app.utils import DuplicateItemError
from werkzeug.security import generate_password_hash
from mongoengine.errors import DoesNotExist, ValidationError, NotUniqueError

def get_user_info(user: Users) -> Dict[str, Any]:
    try:
        return {
            'id': str(user.id),
            'email': user.email,
            'username': user.username
        }
    except Exception as e:
        print(f'Error creating user info {e}')
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

        user = Users(
            username=username,
            email=email,
            password=_password,
        )
        user.save()

        user_info = get_user_info(user=user)

        return user_info
    
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
    user = Users.objects(id=user_id).first()
    user_info = get_user_info(user=user)
    return user_info

# Get user by email
def get_user_by_email(email):
    user = Users.objects(email=email).first()
    user_info = get_user_info(user=user)
    return user_info

# Get all users
def get_users():
    users = Users.objects.all()
    user_infos = [get_user_info(user=u) for u in users]
    return user_infos

# Update an user
def update_user(user_id, **kwargs):
    user = Users.objects(id=user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
    user_info = get_user_info(user=user)
    return user_info

# Delete an user
def delete_user(user_id):
    user = Users.objects(id=user_id).first()
    if not user:
        raise ValueError("User Not Found")
    if user:
        user.delete()
    return True

# Validate user
def validate_user(user_id: str) -> bool:
    """ User verification """
    try:
        user = Users.objects.only('id').get(id=user_id)
        return True
    except (DoesNotExist, ValidationError) as e:
        print(f'User validation failed: {e}')
        return False
    except Exception as e:
        print(f'Unexpected error occurred during user validation: {e}')
        return False