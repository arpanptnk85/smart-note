from app.models import Users
from typing import Any

# Create an user
def create_user(username: str, password: str, email: str) -> Any:
    user = Users(
        username=username,
        email=email,
        password=password,
    )
    user.save()
    return user

# Get user by _id
def get_user_by_id(user_id):
    return Users.objects(id=user_id).first()

# Get user by email
def get_user_by_email(email):
    return Users.objects(email=email).first()

# Get all users
def get_users():
    return Users.objects.all()

# Update an user
def update_user(user_id, **kwargs):
    user = Users.objects(id=user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
    return user

# Delete an user
def delete_user(user_id):
    user = Users.objects(id=user_id).first()
    if user:
        user.delete()
    return user