from locust import HttpLocust, TaskSet, task, between
from faker import Faker
fake = Faker()

class APICalls(TaskSet):    
    @task()
    def getpost(self):
        post_id = fake.random_int(min=1, max=100, step=1)
        self.client.get("/posts/%i" % post_id, name="/posts/[id]")

    @task()
    def postpost(self):        
        self.client.post("/posts", {"title": "foo", "body": "bar", "userId": 1}, name="/posts")

class APIUser(HttpLocust):
    task_set = APICalls
    wait_time = between(5, 10) # seconds