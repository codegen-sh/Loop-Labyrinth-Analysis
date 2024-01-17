from services.auth_service import authenticate_user


def validate_credentials(user):
    # Validate user credentials
    return authenticate_user()
