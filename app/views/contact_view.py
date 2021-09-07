from flask import Flask, request
from app.models.contact_model import Contact


def init_app(app: Flask):

    # TODO: Treat strings
    # TODO: find a way to remove _id from mongo and return the message
    @app.post("/form")
    def post_form_data():
        name = request.form.get("name")
        email = request.form.get("email")
        telephone = request.form.get("telephone")
        message = request.form.get("message")

        contact = Contact(name, email, telephone, message)
        contact = contact.save_contact()
        # for key in contact:
        #     del key["_id"]
        print(contact)

        # final_dict = {
        #     "name": name,
        #     "email": email,
        #     "telephone": int(telephone),
        #     "message": message
        #     }
        # print(final_dict)

        return "Contact saved with success", 200
