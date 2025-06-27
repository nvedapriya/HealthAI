import streamlit as st
from disease_prediction import predict_disease
from treatment_plan import generate_treatment_plan

def display_disease_prediction(model):
    # Disease Prediction
    st.subheader("🧬 Disease Prediction System")
    symptoms_input = st.text_area("Current Symptoms", "Describe symptoms in detail")
    age = st.slider("Age", 0, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    medical_history = st.text_area("Medical History (comma-separated)")
    if st.button("Generate Prediction"):
        with st.spinner("Predicting..."):
            result = predict_disease(symptoms_input, age, gender, medical_history)
            st.markdown("### AI Predicted Conditions")
            st.markdown(result)


def display_treatment_plans(model):
    # Treatment Plan
    st.subheader("🩺 Personalized Treatment Plan Generator")
    condition = st.text_input("Medical Condition", "Mouth Ulcer")
    age = st.slider("Age", 0, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    medical_history = st.text_area("Medical History (comma-separated)")
    if st.button("Generate Treatment Plan"):
        with st.spinner("Generating..."):
            plan = generate_treatment_plan(condition, age, gender, medical_history)
            st.markdown("### AI-Generated Plan")
            st.code(plan, language="markdown")

def display_health_analytics():
    # Health Analytics Dashboard
    st.subheader("📊 Health Analytics Dashboard")
    
    # Sample data
    import pandas as pd
    import plotly.express as px

    df = pd.DataFrame({
        "Day": list(range(1, 8)),
        "Heart Rate": [70, 72, 75, 74, 76, 78, 77],
        "Systolic": [120, 122, 121, 123, 124, 125, 122],
        "Diastolic": [80, 82, 81, 83, 82, 81, 80],
        "Glucose": [90, 95, 92, 94, 96, 93, 91],
        "Symptoms": ["Fatigue", "Cough", "Fever", "Fever", "Fatigue", "Headache", "Fever"]
    })

    # Heart rate
    fig1 = px.line(df, x="Day", y="Heart Rate", title="Heart Rate Over Time")
    st.plotly_chart(fig1)

    # Blood pressure
    fig2 = px.line(df, x="Day", y=["Systolic", "Diastolic"], title="Blood Pressure Trends")
    st.plotly_chart(fig2)

    # Glucose levels
    fig3 = px.line(df, x="Day", y="Glucose", title="Blood Glucose Levels")
    fig3.add_hline(y=100, line_dash="dot", line_color="red", annotation_text="Normal Range")
    st.plotly_chart(fig3)
def display_patient_chat():
    # Patient Chat
    st.subheader("💬 Patient Chat Interface")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="user_input")
    if st.button("Send") and user_input:
        st.session_state.chat_history.append(("You", user_input))
        # Simulate bot response
        response = "I'm processing your message..."
        st.session_state.chat_history.append(("Bot", response))

    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

