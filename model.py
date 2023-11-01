from pydantic.dataclasses import dataclass
from datetime import date

@dataclass
class Task:
    """Dictionary that represents a task."""

    finished: bool
    description: str
    deadline: date
    id: int | None = None
