import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model

def init_granite_model():
    load_dotenv()

    watson_url = os.getenv("IBM_WATSON_URL")
    username = os.getenv("IBM_CP4D_USERNAME")
    password = os.getenv("IBM_CP4D_PASSWORD")

    if not watson_url or not username or not password:
        raise ValueError("Missing one or more required environment variables.")

    credentials = {
        "url": watson_url,
        "username": username,
        "password": password,
        "instance_id": "openshift"
    }

    model = Model(
        model_id="granite-13b-instruct-v2",
        params={"decoding_method": "greedy"},
        credentials=credentials
    )

    return model

# ✅ 1. Patient Chat Function
def answer_patient_query(query: str) -> str:
    model = init_granite_model()
    
    prompt = (
        f"You are a virtual healthcare assistant. A patient has asked:\n"
        f"\"{query}\"\n"
        f"Please respond clearly and kindly in a way understandable by a non-expert. "
        f"Keep it medically sound and safe."
    )
    
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']

# ✅ 2. Disease Prediction Function
def predict_disease(symptoms: str, age: int, gender: str) -> str:
    model = init_granite_model()
    
    prompt = (
        f"A {age}-year-old {gender} presents with the following symptoms: {symptoms}.\n"
        f"List potential (not definitive) health conditions with possible causes. "
        f"Include recommendations and when to see a doctor."
    )
    
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']

# ✅ 3. Treatment Plan Function
def generate_treatment_plan(condition: str, details: str = "") -> str:
    model = init_granite_model()
    
    prompt = (
        f"Create a treatment plan for a patient diagnosed with {condition}.\n"
        f"Patient details: {details}\n"
        f"Include medications (if applicable), lifestyle suggestions, and follow-up recommendations."
    )
    
    response = model.generate(prompt=prompt)
    return response['results'][0]['generated_text']
