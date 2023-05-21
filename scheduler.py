from centralized_algorithms.fcfs import FirstComeFirstServed
from centralized_algorithms.rr import RoundRobin
from data_loader import DataLoader
import random

from decentralized_algorithms.bee import BeeColonyOptimization

n_nodes = 5
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

#peer-to-peer network
# for i in range(5):
#     #each node has 5 peers
#     for node in nodes:
#         n = random.randint(0,19)
#         node.connect_to_peer(nodes[n])

scheduler = FirstComeFirstServed()
scheduler.allocate_resources(jobs, nodes)

for job in jobs:
    for task in job.tasks:
        print(f"Task {task.id} from job {task.job_id} was allocated to node {task.allocated_node}, started at {task.start_time} and ended at {task.finish_time}.")

print(f"\nMakespan for the job set is: {scheduler.makespan}")

