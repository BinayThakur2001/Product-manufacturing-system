import matplotlib.pyplot as plt

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Sort jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    time_slots = [False] * (max_deadline + 1)
    job_order = [None] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:
        # Find a free slot before job's deadline
        for t in range(job.deadline, 0, -1):
            if not time_slots[t]:
                time_slots[t] = True
                job_order[t] = job
                total_profit += job.profit
                break

    scheduled_jobs = [job for job in job_order if job is not None]
    return scheduled_jobs, total_profit


def visualize_schedule(jobs):
    fig, ax = plt.subplots()
    y = 1
    for i, job in enumerate(jobs):
        ax.broken_barh([(i, 0.8)], (y, 0.5), facecolors='tab:blue')
        ax.text(i + 0.3, y + 0.25, job.job_id, fontsize=10, color='white')
    ax.set_xlim(0, len(jobs))
    ax.set_ylim(0, 3)
    ax.set_xlabel("Time Slots")
    ax.set_yticks([])
    ax.set_title("Factory Job Schedule")
    plt.show()


# Example usage
if __name__ == "__main__":
    jobs = [
        Job('A', 2, 100),
        Job('B', 1, 19),
        Job('C', 2, 27),
        Job('D', 1, 25),
        Job('E', 3, 15)
    ]

    print("Available Product Orders:")
    print("Job\tDeadline\tProfit")
    for j in jobs:
        print(f"{j.job_id}\t{j.deadline}\t\t{j.profit}")

    scheduled_jobs, total_profit = job_sequencing(jobs)

    print("\nSelected Manufacturing Order:")
    for job in scheduled_jobs:
        print(f"Job {job.job_id} (Deadline: {job.deadline}, Profit: {job.profit})")

    print(f"\nTotal Profit Earned = {total_profit}")

    visualize_schedule(scheduled_jobs)
