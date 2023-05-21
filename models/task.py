from datetime import datetime, timedelta

class Task:
    def __init__(self, id, job_id, cpu_units, memory, duration, timestamp):
        self.id = id
        self.job_id = job_id
        self.cpu_units = cpu_units
        self.memory = memory
        self.duration = timedelta(minutes=duration) # duration should be in minutes
        self.arrival_time = datetime.fromtimestamp(timestamp)
        self.allocated_node = None
        self.start_time = None
        self.finish_time = None

    @property
    def is_executed(self):
        return self.start_time is not None and self.finish_time is not None and \
               datetime.now() >= self.finish_time

    def __str__(self):
        return "Task {} from job {} with {} CPU units and {} MB of memory".format(self.id, self.job_id, self.cpu_units, self.memory)

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