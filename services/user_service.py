from models.user import User
from services.auth_service import authenticate_user
from utils.common import some_util_function


def get_user():
    # Additional logic here
    authenticate_user()  # New addition
    return User.get_user_info()
