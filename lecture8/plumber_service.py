class PlumberService:
    def __init__(self):
        self.jobs = []

    def add_job_request(self, address, expected_hours_work):
        self.jobs.append((address, expected_hours_work))

    def pickup_job_request(self, hours_available):
        for i, (address, expected_hours_work) in enumerate(self.jobs):
            if expected_hours_work <= hours_available:
                del self.jobs[i]
                return address

    def num_pending_jobs(self):
        return len(self.jobs)

    def hours_work_pending(self):
        hours_work = 0
        for _, expected_hours_work in self.jobs:
            hours_work += expected_hours_work

        return hours_work


sf_plumber_service = PlumberService()
sf_plumber_service.add_job_request("1111 Howard St", 1.5)
sf_plumber_service.add_job_request("234 California St", 0.5)
sf_plumber_service.add_job_request("100 Grant Ave", 2.0)

print(sf_plumber_service.pickup_job_request(1))
print(sf_plumber_service.pickup_job_request(2))

sf_plumber_service.add_job_request("1010 Pine St", 1.0)

print(sf_plumber_service.pickup_job_request(1))
print(sf_plumber_service.num_pending_jobs())
print(sf_plumber_service.hours_work_pending())

