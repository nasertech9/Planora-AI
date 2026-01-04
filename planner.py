class Planner:
    def __init__(self, tasks):
        self.tasks = tasks
        self.completed = set()

    def score(self, task):
        score = 0
        score += task.priority * 10
        if task.deadline:
            score += 5
        score -= len(task.dependencies) * 3
        return score

    def resolve_dependencies(self, task):
        return all(dep in self.completed for dep in task.dependencies)

    def plan(self):
        return sorted(
            self.tasks,
            key=lambda t: self.score(t),
            reverse=True
        )
