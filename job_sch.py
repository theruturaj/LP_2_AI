def schedule_jobs(jobs):
    sorted_jobs = sorted(jobs, key = lambda x: x[1], reverse = True)
    schedule = []
    current_time = 0
    
    for job in sorted_jobs:
        job_id,profit,duration = job
        start_time = current_time
        finish_time = current_time+duration
        current_time = finish_time
        schedule.append((job_id, start_time,finish_time))
        
    return schedule
   
nums_jobs = int(input("enter the no of jobs:"))
jobs = []
for i in range(nums_jobs):
    job_id = int(input(f"enter the job id for job {i+1} \n"))
    profit = int(input(f"enter the profit for job {i+1} \n"))
    duration = int(input(f"enter the duration for job {i+1} \n"))
    jobs.append((job_id,profit,duration))
    
schedule = schedule_jobs(jobs)

for job in schedule:
    print(f"job {job[0]} : start time = {job[1]} : finish time = {job[2]}")