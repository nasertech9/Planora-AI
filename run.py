from datetime import datetime
from task import Task
from scheduler import Scheduler
from planner import Planner

tasks = [
    Task(
        name="Write report",
        duration_minutes=90,
        priority=3,
        deadline=datetime(2026, 1, 5, 18, 0)
    ),
    Task(
        name="Email client",
        duration_minutes=15,
        priority=5
    ),
    Task(
        name="Prepare slides",
        duration_minutes=60,
        priority=4,
        dependencies=["Write report"]
    )
]

planner = Planner(tasks)
scheduler = Scheduler(start_time=datetime(2026, 1, 5, 9, 0))

for task in planner.plan():
    if planner.resolve_dependencies(task):
        if scheduler.add_task(task):
            planner.completed.add(task.name)

print("\n📅 Final Schedule:\n")
for task, time in scheduler.schedule:
    print(f"{time.strftime('%H:%M')} → {task.name}")
