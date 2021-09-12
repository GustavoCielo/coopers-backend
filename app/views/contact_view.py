from flask import Flask, request
from app.models.contact_model import Contact


def init_app(app: Flask):

    @app.post("/form")
    def post_form_data():
        name = request.form.get("name")
        email = request.form.get("email")
        telephone = request.form.get("telephone")
        message = request.form.get("message")

        contact = Contact(name, email, telephone, message)
        contact = contact.save_contact()

        return "Contact saved with success", 200
