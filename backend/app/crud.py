from app.models import User
from typing import Any

# Create an user
def create_user(username: str, password: str, email: str) -> Any:
    user = User(
        username=username,
        email=email,
        password=password,
    )
    user.save()
    return user

# Get user by _id
def get_user_by_id(user_id):
    return User.objects(id=user_id).first()

# Get user by email
def get_user_by_email(email):
    return User.objects(email=email).first()

# Get all users
def get_users():
    return User.objects.all()

# Update an user
def update_user(user_id, **kwargs):
    user = User.objects(id=user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
    return user

# Delete an user
def delete_user(user_id):
    user = User.objects(id=user_id).first()
    if user:
        user.delete()
    return user