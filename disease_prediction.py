import streamlit as st
from granite_model import predict_disease

def display_disease_prediction(model=None):
    st.subheader("🩺 Disease Prediction Based on Symptoms")

    with st.form("disease_form"):
        symptoms = st.text_input("Enter patient symptoms:")
        age = st.number_input("Enter age", min_value=0, step=1)
        gender = st.selectbox("Select gender", ["Male", "Female", "Other"])
        submitted = st.form_submit_button("Predict")

    if submitted and symptoms:
        try:
            result = predict_disease(symptoms, age, gender)  # ✅ Now passing all args
            st.success(f"Predicted Disease: {result}")
        except Exception as e:
            st.error(f"⚠ An error occurred: {e}")