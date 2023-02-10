class Job:
    def __init__(self, job_id, start_time, run_time,tasks):
        self.job_id = job_id
        self.start_time = start_time
        self.run_time = run_time
        self.turn_around_time = start_time + run_time
        self.tasks = tasks

    def __str__(self):
        return "Job {} with tasks {}".format(self.job_id, [str(task) for task in self.tasks])



