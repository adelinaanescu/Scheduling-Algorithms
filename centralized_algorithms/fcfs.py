class FirstComeFirstServed:
    def allocate_resources(self, jobs, containers):

        # Sort jobs in the order they arrive
        jobs.sort(key=lambda x: x.job_id)

        # Allocate resources to each job's tasks
        for job in jobs:
            for task in job.tasks:
                task_allocated = False
                for container in containers:
                    if container.allocate_resources(task):
                        print(f"Task {task.task_id} from job {job.job_id} is allocated to container {container.container_id}")
                        task_allocated = True
                        break
                if not task_allocated:
                    print("Task {} from job {} could not be allocated to any container".format(task.task_id, job.job_id))