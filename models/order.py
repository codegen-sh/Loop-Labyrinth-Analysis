from services.user_service import get_user
from services.product_service import get_product


class Order:
    @staticmethod
    def create_order():
        user = get_user()
        product = get_product()
        # Logic to create an order
        return {'order_id': 789, 'user': user, 'product': product}
