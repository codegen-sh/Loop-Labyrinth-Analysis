from flask import Blueprint
from services.user_service import get_user

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users')
def users():
    return get_user()
