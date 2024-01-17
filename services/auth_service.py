from models.user import User
from utils.auth_utils import validate_credentials


def authenticate_user():
    # Logic for user authentication
    user = User.get_user_info()
    return validate_credentials(user)
