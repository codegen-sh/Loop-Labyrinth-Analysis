from flask import Blueprint
from services.auth_service import authenticate_user

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/authenticate')
def authenticate():
    return authenticate_user()
