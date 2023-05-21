class FirstComeFirstServed:
    def __init__(self):
        self.makespan = None

    def allocate_resources(self, jobs, nodes):
        # Flatten all tasks from all jobs into a single list and sort them
        tasks = sorted([task for job in jobs for task in job.tasks], key=lambda x: x.arrival_time)
        unallocated_tasks = tasks.copy()

        # While there are tasks that have not been allocated, continue to attempt allocation
        while unallocated_tasks:
            for task in unallocated_tasks:
                for node in nodes:
                    # deallocate resources for completed tasks
                    node.deallocate_resources()
                    # allocate resources to new task
                    if node.allocate_resources(task):
                        # If the task is allocated, store the node ID
                        task.allocated_node = node.node_id
                        unallocated_tasks.remove(task)
                        break
                # If all nodes have been tried, and task is not allocated, wait before next attempt
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
