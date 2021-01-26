import random
from locust import HttpUser, task

class HotRod(HttpUser):
    def on_start(self):
        pass

    @task
    def rachels_floral_designs(self):
        nonse = str(random.uniform(0,1))
        self.client.get("/config?nonse=" + nonse)
        customer_id = "123"
        nonse = str(random.uniform(0,1))
        self.client.get("/dispatch?customer=" + customer_id + "&nonse=" + nonse)

    @task
    def amazing_coffee_roasters(self):
        nonse = str(random.uniform(0,1))
        self.client.get("/config?nonse=" + nonse)
        customer_id = "567"
        nonse = str(random.uniform(0,1))
        self.client.get("/dispatch?customer=" + customer_id + "&nonse=" + nonse)

    @task
    def trom_chocolatier(self):
        nonse = str(random.uniform(0,1))
        self.client.get("/config?nonse=" + nonse)
        customer_id = "392"
        nonse = str(random.uniform(0,1))
        self.client.get("/dispatch?customer=" + customer_id + "&nonse=" + nonse)

    @task
    def japanese_desserts(self):
        nonse = str(random.uniform(0,1))
        self.client.get("/config?nonse=" + nonse)
        customer_id = "731"
        nonse = str(random.uniform(0,1))
        self.client.get("/dispatch?customer=" + customer_id + "&nonse=" + nonse)
