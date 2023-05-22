from datetime import timedelta

from centralized_algorithms.fcfs import FirstComeFirstServed
from centralized_algorithms.sjf import ShortestJobFirst

from data_loader import DataLoader
import random

from decentralized_algorithms.bee import BeeColonyOptimization

n_nodes = 10
n_tasks = 45
n_jobs = 20

dataLoader = DataLoader()
jobs = dataLoader.jobs_loader(n_jobs)
tasks = dataLoader.tasks_loader(n_tasks)

for job in jobs:
 for task in tasks:
     if job.id == task.job_id:
         job.tasks.append(task)

nodes = dataLoader.nodes_loader(n_nodes)

# Build network
for node in nodes:
    # Create a copy of the nodes list and remove the current node
    other_nodes = nodes.copy()
    other_nodes.remove(node)
    # Randomly select 5 nodes to be neighbors of the current node
    neighbors = random.sample(other_nodes, 5)
    for neighbor in neighbors:
        node.add_neighbor(neighbor)


scheduler = BeeColonyOptimization(10,10,10)
scheduler.allocate_resources(jobs, nodes[1])

for job in jobs:
    for task in job.tasks:
        print(f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")

print(f"\nMakespan for the job set is: {scheduler.makespan}")

