from flask import Flask, request, jsonify
from app.models.task_model import Task

"""Routes for api"""


def init_app(app: Flask):

    @app.get("/")
    def get_all_tasks():
        task = Task.get_all_tasks()
        return jsonify(task), 200

    @app.post("/")
    def create_task():
        """Create a task through post request,
        instances the Task class, validating all info and returning the task"""
        data = request.get_json()
        task = Task(**data)
        task.create_and_save_task()
        return task.__dict__, 200

    @app.delete("/<string:id>")
    def delete_task_by_id(id: str):
        Task.delete_task_by_id(id)
        return {"msg": "Task deleted with success"}, 200

    @app.patch("/<string:id>")
    def update_task_by_id(id: str):
        """method to update task_content and task_done"""
        data = request.get_json()
        Task.update_task_by_id(id, data)

        return {"msg": "Task updated with success"}, 200

    @app.delete("/eraseall/<string:value>")
    def delete_all(value: str):
        """returns a string with value for true or false,
        then checks the value in dict and sends to the mongoDB"""

        new_dict = {
            "todo": False,
            "done": True
        }

        return Task.delete_all_tasks_by_boolean(new_dict[value])
