from time import sleep
from faker import Faker
from celery import shared_task
import json

@shared_task
def add(x, y):
    sleep(2)
    x  = int(x)
    y = int(y)
    return x + y 

@shared_task
def mul(x, y):
    return x * y


@shared_task
def generate_fake_data(limit: int = 10, /, fake = Faker()) -> list[dict]:

    data = [
        {
            "name": fake.name(),
            "address": fake.address(),
            "text": fake.text()
        } for _ in range(limit)
    ]

    return data