from centralized_algorithms.fcfs import FirstComeFirstServed
from data_loader import DataLoader
import random

from decentralized_algorithms.bee import BeeColonyOptimization
n_nodes = 20
n_tasks = 50
n_jobs = 20

dataLoader = DataLoader()
jobs = dataLoader.jobs_loader(n_jobs)
tasks = dataLoader.tasks_loader(n_tasks)
nodes = dataLoader.nodes_loader(n_nodes)

#peer-to-peer network
for i in range(5):
    #each node has 5 peers
    for node in nodes:
        n = random.randint(0,19)
        node.connect_to_peer(nodes[n])

# fcfs = FirstComeFirstServed()
# fcfs.allocate_resources(jobs, nodes)

# bco = BeeColonyOptimization()
# bco.allocate_resources(jobs, nodes)
