import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_data(days=30):
    today = datetime.today()
    data = []

    for i in range(days):
        date = today - timedelta(days=i)
        bp = random.randint(110, 150)
        hr = random.randint(60, 100)
        data.append({"date": date.strftime("%Y-%m-%d"), "blood_pressure": bp, "heart_rate": hr})

    df = pd.DataFrame(data)
    df.to_csv("data/sample_patient_data.csv", index=False)