from datetime import datetime, timedelta
from collections import deque

class FirstComeFirstServed:
    def __init__(self):
        self.makespan = None
        self.current_time = datetime.min  # Initialize current time at the minimum datetime value

    def allocate_resources(self, jobs, starting_node):
        tasks = sorted([task for job in jobs for task in job.tasks], key=lambda x: x.arrival_time)
        unallocated_tasks = tasks.copy()

        queue = deque([starting_node])

        while unallocated_tasks:
            if queue:
                node = queue.popleft()
                node.deallocate_resources(self.current_time)

                for task in unallocated_tasks:
                    self.current_time = max(self.current_time, task.arrival_time)
                    if node.allocate_resources(task, self.current_time):
                        task.allocated_node = node.node_id
                        print(
                            f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")
                        unallocated_tasks.remove(task)
                        queue.extend(
                            node.neighbors)  # Add the neighbors of this node to the queue only if the node could take a task
                        break
            else:
                self.current_time += timedelta(seconds=1)
                queue = deque([starting_node])  # Reset the queue with the starting node

        self.makespan = self.compute_makespan(tasks)

    def compute_makespan(self, tasks):
        finish_times = []
        for task in tasks:
            if task.is_executed:
                finish_times.append(task.finish_time)
        if finish_times:
            makespan = max(finish_times) - min(task.arrival_time for task in tasks)
            return makespan.total_seconds()
