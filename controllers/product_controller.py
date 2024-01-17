from flask import Blueprint
from services.product_service import get_product

product_routes = Blueprint('product_routes', __name__)


@product_routes.route('/products')
def products():
    return get_product()
