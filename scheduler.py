from centralized_algorithms.fcfs import FirstComeFirstServed
from data_loader import DataLoader

dataLoader = DataLoader()
jobs = dataLoader.jobs_loader(20)
tasks = dataLoader.tasks_loader(50)
nodes = dataLoader.nodes_loader(20)

# fcfs = FirstComeFirstServed()
# fcfs.allocate_resources(jobs,nodes)