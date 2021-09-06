from pymongo import MongoClient
import os
from dotenv import load_dotenv


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
    def __init__(self, task_done: bool, task_content: str):
        self.task_done = task_done
        task_content = task_content
        # self.id

    def create_and_save_task():
        ...

    def delete_task_by_id():
        ...

    def delete_all_tasks_by_boolean():
        ...

    def update_task_by_id():
        ...
