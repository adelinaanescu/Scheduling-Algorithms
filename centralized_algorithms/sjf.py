from datetime import datetime, timedelta

class ShortestJobFirst:
    def __init__(self):
        self.makespan = None
        self.current_time = datetime.min  # Initialize current time at the minimum datetime value

    def allocate_resources(self, jobs, nodes):
        # Flatten all tasks from all jobs into a single list and sort them
        tasks = sorted([task for job in jobs for task in job.tasks], key=lambda x: (x.duration, x.arrival_time))
        unallocated_tasks = tasks.copy()

        # While there are tasks that have not been allocated, continue to attempt allocation
        while unallocated_tasks:
            for task in unallocated_tasks:
                # Advance the global current time to the arrival time of the next task
                self.current_time = max(self.current_time, task.arrival_time)
                for node in nodes:
                    # deallocate resources for completed tasks
                    node.deallocate_resources(self.current_time)
                    # allocate resources to new task
                    if node.allocate_resources(task, self.current_time):
                        # If the task is allocated, store the node ID
                        task.allocated_node = node.node_id
                        print(f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")
                        unallocated_tasks.remove(task)
                        break
                else:
                    # If all nodes have been tried, and task is not allocated, increment current time
                    self.current_time += timedelta(seconds=1)
                    continue

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
