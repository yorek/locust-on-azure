from locust import HttpLocust, TaskSet, task, between
from faker import Faker
fake = Faker()

class UserBehavior(TaskSet):
    @task()
    def customer(self):
        customer_id = fake.random_int(min=1, max=1061, step=1)
        self.client.get("/customer/%i" % customer_id, name="/customer/[id]")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(0.1, 0.2)