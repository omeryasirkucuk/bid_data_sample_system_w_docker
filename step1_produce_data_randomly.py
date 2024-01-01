# pip install faker
from faker import Faker
import json
import pandas as pd
import time

fake = Faker()


def generate_data():
    sampledata = []
    try:
        while True:
            record = {
                'name': fake.name(),
                'email': fake.email(),
                'address': fake.address(),
                'phone_number': fake.phone_number()
            }
            sampledata.append(record)
            with open("D:\Works\Docker\Projects\Big Data Sample System\sample_data.json", 'w') as file:
                json.dump(sampledata, file, indent=2)
            time.sleep(10)
    except KeyboardInterrupt:
        return sampledata

data = generate_data()
