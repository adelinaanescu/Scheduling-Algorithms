class Task:
    def __init__(self, id, job_id, cpu_units, memory):
        self.id = id
        self.job_id = job_id
        self.cpu_units = cpu_units
        self.memory = memory


    def __str__(self):
        return "Task {}  from {} job with {} CPU units and {} MB of memory".format(self.id, self.job_id, self.cpu_units, self.memory)


# The task events table contains the following fields:
# 1. timestamp
# 2. missing info
# 3. job ID
# 4. task index - within the job
# 5. machine ID
# 6. event type
# 7. user name
# 8. scheduling class
# 9. priority
# 10. resource request for CPU cores
# 11. resource request for RAM
# 12. resource request for local disk space
# 13. different-machine constraint