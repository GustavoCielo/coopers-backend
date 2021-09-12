from flask import Flask
from flask_cors import CORS


def create_app(app: Flask):
    app = Flask(__name__)
    CORS(app)

    from app.views import task_view, contact_view

    task_view.init_app(app)

    contact_view.init_app(app)

    return app
