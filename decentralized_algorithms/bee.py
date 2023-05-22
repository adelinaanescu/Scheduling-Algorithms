from datetime import datetime, timedelta
from collections import deque
import random

class BeeColonyOptimization:
    def __init__(self, num_employed_bees, num_onlooker_bees, num_scout_bees):
        self.num_employed_bees = num_employed_bees
        self.num_onlooker_bees = num_onlooker_bees
        self.num_scout_bees = num_scout_bees
        self.makespan = None
        self.current_time = datetime.min  # Initialize current time at the minimum datetime value

    def allocate_resources(self, jobs, initial_node):
        tasks = sorted([task for job in jobs for task in job.tasks], key=lambda x: x.arrival_time)
        unallocated_tasks = tasks.copy()

        employed_bees = [EmployedBee() for _ in range(self.num_employed_bees)]
        onlooker_bees = [OnlookerBee() for _ in range(self.num_onlooker_bees)]
        scout_bees = [ScoutBee() for _ in range(self.num_scout_bees)]
        all_bees = employed_bees + onlooker_bees + scout_bees


        # Randomly assign bees to nodes
        for bee in all_bees:
            bee.assigned_node = initial_node


        queue = deque([initial_node])

        while unallocated_tasks:
            if queue:
                node = queue.popleft()
                node.deallocate_resources(self.current_time)

                for bee in employed_bees:
                    task_index = bee.task_index % len(unallocated_tasks)
                    task = unallocated_tasks[task_index]

                    self.current_time = max(self.current_time, task.arrival_time)
                    if node.allocate_resources(task, self.current_time):
                        task.allocated_node = node.node_id
                        print(
                            f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")
                        unallocated_tasks.remove(task)
                        bee.task_index += 1

                        if bee.task_index == len(unallocated_tasks):
                            # All tasks assigned to this bee, reset its task index
                            bee.task_index = 0

                        queue.extend(
                            node.neighbors)  # Add the neighbors of this node to the queue only if the node could take a task
                        break

            # Onlooker bees observe the employed bees and select tasks based on fitness values
            for bee in onlooker_bees:
                selected_bee = self.select_bee_based_on_fitness(employed_bees)
                if len(unallocated_tasks) == 0:
                    break
                task_index = selected_bee.task_index % len(unallocated_tasks)
                task = unallocated_tasks[task_index]

                self.current_time = max(self.current_time, task.arrival_time)
                if node.allocate_resources(task, self.current_time):
                    task.allocated_node = node.node_id
                    print(
                        f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")
                    unallocated_tasks.remove(task)
                    selected_bee.task_index += 1

                    if selected_bee.task_index == len(unallocated_tasks):
                        # All tasks assigned to this bee, reset its task index
                        selected_bee.task_index = 0

                    queue.extend(node.neighbors)  # Add the neighbors of this node to the queue only if the node could take a task
                    break

            # Scout bees discover new solutions by exploring unallocated tasks randomly
            for bee in scout_bees:
                if len(unallocated_tasks) == 0:
                    break
                task = random.choice(unallocated_tasks)

                self.current_time = max(self.current_time, task.arrival_time)
                if node.allocate_resources(task, self.current_time):
                    task.allocated_node = node.node_id
                    print(
                        f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")
                    unallocated_tasks.remove(task)

                    queue.extend(
                        node.neighbors)  # Add the neighbors of this node to the queue only if the node could take a task
                    break

            if not queue:
                self.current_time += timedelta(seconds=1)
                queue = deque([initial_node])  # Reset the queue with all nodes

        self.makespan = self.compute_makespan(tasks)

    def select_bee_based_on_fitness(self, bees):
        total_fitness = sum(bee.fitness for bee in bees)

        if total_fitness == 0:
            # If total fitness is zero, assign equal probabilities to all bees
            probabilities = [1 / len(bees)] * len(bees)
        else:
            probabilities = [bee.fitness / total_fitness for bee in bees]

        selected_bee = random.choices(bees, probabilities)[0]
        return selected_bee

    def compute_makespan(self, tasks):
        finish_times = []
        for task in tasks:
            if task.is_executed:
                finish_times.append(task.finish_time)
        if finish_times:
            makespan = max(finish_times) - min(task.arrival_time for task in tasks)
            return makespan.total_seconds()


class EmployedBee:
    def __init__(self):
        self.assigned_node = None
        self.task_index = 0
        self.fitness = 0

    def calculate_fitness(self, tasks):
        # Calculate the fitness value based on the makespan
        finish_times = [task.finish_time for task in tasks if task.is_executed]
        if finish_times:
            makespan = max(finish_times) - min(task.arrival_time for task in tasks)
            self.fitness = 1 / makespan.total_seconds()  # Inverse of makespan
        else:
            self.fitness = 0


class OnlookerBee:
    def __init__(self):
        self.assigned_node = None
        self.fitness = 0

class ScoutBee:
    def __init__(self):
        self.assigned_node = None
        self.fitness = 0
