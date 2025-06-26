import pandas as pd
import random
from datetime import datetime, timedelta

# Generate dummy patient health metrics over 30 days
def get_patient_data():
    dates = [datetime.now() - timedelta(days=i) for i in range(30)][::-1]
    data = pd.DataFrame({
        'Date': dates,
        'HeartRate': [random.randint(60, 100) for _ in dates],
        'BloodPressure': [random.randint(110, 140) for _ in dates]
    })
    return data

# Generate simple AI insights from trends
def generate_ai_insights(data: pd.DataFrame) -> str:
    avg_hr = data['HeartRate'].mean()
    avg_bp = data['BloodPressure'].mean()

    insight = (
        f"🧠 Health Insight:\n"
        f"- Average Heart Rate: {avg_hr:.1f} bpm\n"
        f"- Average Blood Pressure: {avg_bp:.1f} mmHg\n\n"
        f"📌 Recommendations:\n"
        f"- Maintain regular physical activity\n"
        f"- Reduce salt and caffeine intake\n"
        f"- Stay hydrated and manage stress"
    )
    return insight
