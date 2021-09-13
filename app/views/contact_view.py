from flask import Flask, request
from app.models.contact_model import Contact


def init_app(app: Flask):

    @app.post("/form")
    def post_form_data():
        data = request.get_json()

        contact = Contact(**data)
        contact = contact.save_contact()

        return "Contact saved with success", 200
