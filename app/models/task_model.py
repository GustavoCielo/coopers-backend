from pymongo import MongoClient
import os
from dotenv import load_dotenv
import uuid


# load environment variables
load_dotenv()

# set env variables as host and port

client = MongoClient(
    os.getenv('DATABASE_URL'),
    int(os.getenv('DATABASE_PORT'))
)

# generate and create mongo DB connection
db = client[os.getenv('DATABASE_NAME')]
# TODO: choose a name for coopers.collection and create it


class Task:
    def __init__(self, task_content: str):
        self.task_done: bool = False
        self.task_content = task_content
        self.id = str(uuid.uuid4())

    def create_and_save_task(self):
        # TODO: treat exceptions and failures

        task = db.tasks.insert_one(self.__dict__)
        del self.__dict__['_id']

        return task

    def delete_task_by_id(id):
        # TODO: treat exceptions and failures

        task = db.tasks.find_one_and_delete({"id": id})

        return {"msg": f'{task} deleted with success'}

    def delete_all_tasks_by_boolean(delete_all_tasks):

        task = db.tasks.delete_many({"task_done": delete_all_tasks})

        return {"msg": f'{task} erased with success'}, 200

    def update_task_by_id():
        ...