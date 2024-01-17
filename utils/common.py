from services.session_service import check_session
from utils.auth_utils import validate_credentials


def some_util_function():
    user = check_session()
    # Additional utility logic
    validate_credentials(user)
