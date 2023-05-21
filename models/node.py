from datetime import datetime


class Node:
    def __init__(self, node_id, cpu_capacity, memory_capacity):
        self.node_id = node_id
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_units_allocated = 0
        self.memory_allocated = 0
        self.tasks = [] # tasks running on this node
        self.current_time = datetime.min  # The current time of this node
        self.neighbors = set()  # Nodes directly connected to this node

    def __str__(self):
        return "Node {} with {} CPU units and {} MB of memory".format(self.node_id, self.cpu_capacity, self.memory_capacity)

    def add_neighbor(self, node):
        """Add a node as a neighbor."""
        # Check if node is already a neighbor
        if node in self.neighbors:
            #print(f"Node {node.node_id} is already a neighbor of Node {self.node_id}.")
            return False

        # Add the node as a neighbor
        self.neighbors.add(node)

        # Also add this node as a neighbor of the new neighbor
        # Check if this node is already a neighbor of the new neighbor
        if self in node.neighbors:
            #print(f"Node {self.node_id} is already a neighbor of Node {node.node_id}.")
            return False

        node.neighbors.add(self)
        return True

    def allocate_resources(self, task, current_time):
        if self.cpu_units_allocated + task.cpu_units <= self.cpu_capacity and \
                self.memory_allocated + task.memory <= self.memory_capacity:
            self.cpu_units_allocated += task.cpu_units
            self.memory_allocated += task.memory
            task.start_time = current_time
            task.finish_time = task.start_time + task.duration
            self.tasks.append(task)
            return True
        return False

    def deallocate_resources(self, current_time):
        for task in self.tasks:
            if task.is_executed and task.finish_time <= current_time:
                self.cpu_units_allocated -= task.cpu_units
                self.memory_allocated -= task.memory
                self.tasks.remove(task)

# Machine events table:
# 1. timestamp
# 2. machine ID
# 3. event type
# 4. platform ID
# 5. capacity: CPU
# 6. capacity: memory