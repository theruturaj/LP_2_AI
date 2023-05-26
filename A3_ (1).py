class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Sort jobs in descending order of profits
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    result = [-1] * n  # Result array to store scheduled jobs
    slots = [False] * n  # Array to keep track of time slots

    # Iterate through all the jobs
    for i in range(n):
        # Find a suitable time slot for the job
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if not slots[j]:
                result[j] = jobs[i].id
                slots[j] = True
                break

    return result

# Example usage:
jobs = [
    Job(1, 2, 100),
    Job(2, 1, 50),
    Job(3, 2, 10),
    Job(4, 1, 20),
    Job(5, 3, 30)
]

scheduled_jobs = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled_jobs)
