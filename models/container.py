class Container:
    def __init__(self, container_id, cpu_capacity, memory_capacity):
        self.container_id = container_id
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_units_allocated = 0
        self.memory_allocated = 0

    def allocate_resources(self, task):
        if self.cpu_units_allocated + task.cpu_units <= self.cpu_capacity and self.memory_allocated + task.memory <= self.memory_capacity:
            self.cpu_units_allocated += task.cpu_units
            self.memory_allocated += task.memory
            return True
        return False

    def deallocate_resources(self, task):
        self.cpu_units_allocated -= task.cpu_units
        self.memory_allocated -= task.memory

    def __str__(self):
        return "Docker container {} with {} CPU units and {} MB of memory".format(self.container_id, self.cpu_capacity,self.memory_capacity)