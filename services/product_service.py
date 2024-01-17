from models.product import Product
from utils.another_util import another_util_function
from services.auth_service import authenticate_user


def get_product():
    authenticate_user()
    another_util_function()
    return Product.get_product_info()
