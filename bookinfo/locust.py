from locust import HttpUser, task

class BookInfo(HttpUser):
    def on_start(self):
        pass

    @task
    def productpage(self):
        self.client.get("/productpage")
