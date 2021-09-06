from flask import Flask


def create_app(app: Flask):
    app = Flask(__name__)

    from app.views import view

    view.init_app(app)

    return app
