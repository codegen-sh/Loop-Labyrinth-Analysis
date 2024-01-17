from controllers.product_controller import product_routes


class Product:
    @staticmethod
    def get_product_info():
        # Fetch product information (Dummy data for example)
        return {'name': 'Example Product', 'id': 456}
