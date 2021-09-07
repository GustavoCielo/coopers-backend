from pymongo import MongoClient
import os
from dotenv import load_dotenv
import uuid

# load environment variables
load_dotenv()

client = MongoClient(
    os.getenv('DATABASE_URL'),
    int(os.getenv('DATABASE_PORT'))
)

# generate and create mongo DB connection
db = client[os.getenv('DATABASE_NAME')]


class Contact:
    def __init__(self, name: str, email: str, telephone: int, message: str):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.message = message
        self.id = str(uuid.uuid4())

    def save_contact(self):
        db.contacts.insert_one(self.__dict__)

        return db.contacts.find_one({"name": self.name})
