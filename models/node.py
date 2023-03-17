class Node:
    def __init__(self, node_id, cpu_capacity, memory_capacity):
        self.node_id = node_id
        self.peers = []
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_units_allocated = 0
        self.memory_allocated = 0

    def __str__(self):
        return "Node {} with {} CPU units and {} MB of memory".format(self.node_id, self.cpu_capacity, self.memory_capacity)

    def connect_to_peer(self, node):
        self.peers.append(node)

    def allocate_resources(self, task):
        if self.cpu_units_allocated + task.cpu_units <= self.cpu_capacity and \
                self.memory_allocated + task.memory <= self.memory_capacity:
            self.cpu_units_allocated += task.cpu_units
            self.memory_allocated += task.memory
            return True
        return False

    def deallocate_resources(self, task):
        self.cpu_units_allocated -= task.cpu_units
        self.memory_allocated -= task.memory

# Machine events table:
# 1. timestamp
# 2. machine ID
# 3. event type
# 4. platform ID
# 5. capacity: CPU
# 6. capacity: memory