from models.order import Order
from utils.common import some_util_function
from services.auth_service import authenticate_user


def process_order():
    some_util_function()
    authenticate_user()  # New addition
    return Order.create_order()
