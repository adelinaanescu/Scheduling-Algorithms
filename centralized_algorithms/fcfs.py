class FirstComeFirstServed:
    def allocate_resources(self, jobs, nodes):

        # Sort jobs in the order they arrive
        jobs.sort(key=lambda x: x.job_id)

        # Allocate resources to each job's tasks
        for job in jobs:
            for task in job.tasks:
                task_allocated = False
                for node in nodes:
                    if node.resource.allocate_resources(task):
                        print(f"Task {task.task_id} from job {job.job_id} is allocated to resource "
                              f"{node.resource.resource_id}")
                        task_allocated = True
                        break
                if not task_allocated:
                    print("Task {} from job {} could not be allocated to any resource".format(task.task_id, job.job_id))