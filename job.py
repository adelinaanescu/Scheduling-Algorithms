from task import Task

class Job:
    def __init__(self, id, tasks):
        self.id = id
        self.tasks = tasks

    def print_tasks(self):
        for task in self.tasks:
            print(task)

    def __str__(self):
        return f"Job(id={self.id}, tasks={self.tasks})"

# Usage
tasks = [Task(1, 2, [1, 2]), Task(2, 3, [2, 3])]
job = Job(1, tasks)
print(job)
job.print_tasks()
