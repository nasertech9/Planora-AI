def respects_deadline(task, start_time):
    if not task.deadline:
        return True
    return start_time + task.duration <= task.deadline


def respects_earliest_start(task, start_time):
    if not task.earliest_start:
        return True
    return start_time >= task.earliest_start
