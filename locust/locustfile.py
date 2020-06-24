from locust import HttpUser, TaskSet, task, between
import random

class APICalls(TaskSet):    
    @task()
    def getpost(self):
        post_id = random.randint(1, 100)
        self.client.get("/posts/%i" % post_id, name="/posts/[id]")

    @task()
    def postpost(self):        
        self.client.post("/posts", {"title": "foo", "body": "bar", "userId": 1}, name="/posts")

class APIUser(HttpUser):
    tasks = [APICalls]
    wait_time = between(5, 10) # seconds