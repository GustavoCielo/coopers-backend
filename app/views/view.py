from flask import Flask, request
from app.models.task import Task


# routes go here
def init_app(app: Flask):

    @app.get("/")
    def get_all_tasks():
        return "Retorna todas as tasks", 200

    @app.post("/")
    def create_task():
        ...
        # cria a task e salva no banco de dados

    @app.delete("/<int:id>")
    def delete_task_by_id(id: int):
        ...
        # deleta a task específica clicada

    @app.delete("/")
    def delete_all():
        ...
        # deleta todas as tasks da lista com base no booleano
