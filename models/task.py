class Task:
    def __init__(self, task_id, cpu_units, memory):
        self.task_id = task_id
        self.cpu_units = cpu_units
        self.memory = memory


    def __str__(self):
        return "Task {} with {} CPU units and {} MB of memory".format(self.task_id, self.cpu_units, self.memory)


