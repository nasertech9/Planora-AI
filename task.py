from datetime import datetime, timedelta

class Task:
    def __init__(
        self,
        name: str,
        duration_minutes: int,
        priority: int = 1,
        deadline: datetime | None = None,
        earliest_start: datetime | None = None,
        dependencies: list[str] = None
    ):
        self.name = name
        self.duration = timedelta(minutes=duration_minutes)
        self.priority = priority
        self.deadline = deadline
        self.earliest_start = earliest_start
        self.dependencies = dependencies or []

    def __repr__(self):
        return f"Task({self.name}, priority={self.priority})"
