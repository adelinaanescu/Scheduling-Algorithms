class Task:
    def __init__(self, arrival_time, duration, requirements):
        self.arrival_time = arrival_time
        self.duration = duration
        self.requirements = requirements

    def __str__(self):
        return f"Task(arrival_time={self.arrival_time}, duration={self.duration}, requirements={self.requirements})"

