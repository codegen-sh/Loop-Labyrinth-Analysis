from controllers.user_controller import user_routes


class User:
    @staticmethod
    def get_user_info():
        # Fetch user information (Dummy data for example)
        return {'name': 'John Doe', 'id': 123}
