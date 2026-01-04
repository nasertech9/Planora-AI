from datetime import timedelta
from constraints import respects_deadline, respects_earliest_start

class Scheduler:
    def __init__(self, start_time):
        self.current_time = start_time
        self.schedule = []

    def can_schedule(self, task, start_time):
        return (
            respects_deadline(task, start_time)
            and respects_earliest_start(task, start_time)
        )

    def add_task(self, task):
        if self.can_schedule(task, self.current_time):
            self.schedule.append((task, self.current_time))
            self.current_time += task.duration
            return True
        return False
