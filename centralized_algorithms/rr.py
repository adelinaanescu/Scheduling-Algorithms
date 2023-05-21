import datetime

class RoundRobin:
    def __init__(self):
        self.makespan = None

    def allocate_resources(self, jobs, nodes):
        # Flatten all tasks from all jobs into a single list and sort them by arrival_time
        tasks = sorted([task for job in jobs for task in job.tasks], key=lambda x: x.arrival_time)
        unallocated_tasks = tasks.copy()

        # While there are tasks that have not been allocated, continue to attempt allocation
        current_node_index = 0
        while unallocated_tasks:
            for task in unallocated_tasks:
                for i in range(len(nodes)):
                    current_node = nodes[current_node_index]
                    current_node.deallocate_resources()
                    if current_node.allocate_resources(task):
                        task.allocated_node = current_node.node_id
                        unallocated_tasks.remove(task)
                        break
                    # Move to next node
                    current_node_index = (current_node_index + 1) % len(nodes)
                # If all nodes have been tried and task is not allocated, wait before next attempt
                if task.allocated_node is None:
                    break

        # Calculate makespan
        self.makespan = self.compute_makespan(tasks)

    def compute_makespan(self, tasks):
        finish_times = []
        for task in tasks:
            if task.is_executed:
                finish_times.append(task.finish_time)
        if finish_times:
            makespan = max(finish_times) - min(task.arrival_time for task in tasks)
            return makespan.total_seconds()
