from datetime import date
from model import Task

tasks = {
    1: Task(id=1, description="Buy milk", finished=False, deadline=date(2023, 12, 31)),
    2: Task(id=2, description="Buy eggs", finished=False, deadline=date(2023, 11, 1)),
}


def add_task(task: Task) -> Task:
    """Add task to database."""
    task_id = max(tasks) + 1
    task.id = task_id
    tasks[task_id] = task
    return task


def delete_task(task_id: int) -> Task | None:
    """Delete task with a given id."""
    current_task = tasks.get(task_id)
    if not current_task:
        return
    return tasks.pop(task_id)


def get_all_tasks() -> list[Task]:
    """Get all tasks."""
    return [task for _, task in tasks.items()]


def update_task(task: Task) -> Task | None:
    """Update task and return it if succesful."""
    if not task.id:
        return
    current_task = tasks.get(task.id)
    if not current_task:
        return
    tasks[task.id] = task
    return task
