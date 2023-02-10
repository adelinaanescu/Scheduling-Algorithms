from models.task import Task
from models.job import Job
from models.container import Container
from centralized_algorithms.fcfs import FirstComeFirstServed

task1 = Task(1, 2, 50)
task2 = Task(2, 3, 70)
task3 = Task(3, 1, 90)

job1 = Job(1, 1,1, [task1, task2])
job2 = Job(2, 1,1, [task3])
jobs=[job1,job2]

c1 = Container(1, 4, 100)
c2 = Container(2, 5, 80)
c3 = Container(3, 3, 60)
containers = [c1, c2, c3]

fcfs = FirstComeFirstServed()
fcfs.allocate_resources(jobs,containers)