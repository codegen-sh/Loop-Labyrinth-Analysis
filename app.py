from flask import Flask
from controllers.user_controller import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)


@app.route('/')
def index():
    return 'Welcome to the Loop Labyrinth!'


if __name__ == '__main__':
    app.run(debug=True)
