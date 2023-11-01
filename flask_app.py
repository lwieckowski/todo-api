from dataclasses import asdict
from flask import Flask, request
from flask_cors import CORS
import db
from model import Task


app = Flask(__name__)
CORS(app)

@app.route("/tasks")
def get_tasks():
    """Get response with all tasks."""
    return db.get_all_tasks()


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    """Delete task and return it if successful."""
    deleted_task = db.delete_task(task_id)
    if not deleted_task:
        return "Bad request", 400
    return asdict(deleted_task)


@app.route("/tasks", methods=["POST"])
def add_task():
    task = Task(**request.get_json())
    added_task = db.add_task(task)
    return asdict(added_task), 201


@app.route("/tasks", methods=["PUT"])
def update_task():
    task = Task(**request.get_json())
    updated_task = db.update_task(task)
    if not updated_task:
        return "Bad request", 400
    return asdict(updated_task)
