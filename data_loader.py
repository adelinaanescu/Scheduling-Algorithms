# extract data from the Google cluster-usage-traces format schema
import csv
from models.job import Job
from models.node import Node
from models.task import Task


class DataLoader:
    def jobs_loader(self, number_of_jobs):
        jobs = []
        with open("database/job_events.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                    id = row[2]
                    event_type = row[3]
                    timestamp = row[0]
                    job = Job(id, timestamp, event_type)
                    # print(job)
                    jobs.append(job)
                    line_count += 1
                    if line_count >= number_of_jobs:
                        break
            return jobs

    def tasks_loader(self, number_of_tasks):
        tasks = []
        with open("database/task_events.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                id = row[3]
                job_id = row[2]
                cpu_units = row[9]
                memory = row[10]
                task = Task(id, job_id, cpu_units, memory)
                # print(task)
                tasks.append(task)
                line_count += 1
                if line_count >= number_of_tasks:
                    break
            return tasks

    def nodes_loader(self, number_of_nodes):
        nodes = []
        with open("database/machine_events.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                id = row[1]
                cpu_capacity = row[4]
                memory_capacity = row[5]
                node = Node(id, cpu_capacity, memory_capacity)
                # print(node)
                nodes.append(node)
                line_count += 1
                if line_count >= number_of_nodes:
                    break
            return nodes