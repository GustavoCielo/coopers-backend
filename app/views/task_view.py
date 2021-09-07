from flask import Flask, request
from app.models.task_model import Task


# routes go here
def init_app(app: Flask):

    @app.get("/")
    def get_all_tasks():
        return "Retorna todas as tasks", 200

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
        # deleta a task específica clicada

    @app.patch("/<string:id>")
    def update_task_by_id(id: str):
        ...
        # encontro a task pelo id e dou patch nela

    # @app.delete("/<bool:delete_all_tasks>")
    # def delete_all(delete_all_tasks: bool):
    #     Task.delete_all_tasks_by_boolean(delete_all_tasks)
    #     # deleta todas as tasks da lista com base no booleano

    @app.post("/form")
    def post_form_data():
        ...
        # get all data from forms and save it on DB
