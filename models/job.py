class Job:
    def __init__(self, id, timestamp, event_type):
        self.id = id
        self.timestamp = timestamp
        self.event_type = event_type


    def __str__(self):
        return "Job with id {}".format(self.id)



# The job events table contains the following fields:
# 1. timestamp
# 2. missing info
# 3. job ID
# 4. event type
# 5. user name
# 6. scheduling class
# 7. job name
# 8. logical job name