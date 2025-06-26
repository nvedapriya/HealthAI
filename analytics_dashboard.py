import streamlit as st
import pandas as pd
import plotly.express as px

def display_health_analytics():
    data = {
        "Disease": ["Diabetes", "Heart Disease", "Hypertension", "Diabetes"],
        "Fever": [1, 0, 0, 1],
        "Cough": [1, 1, 0, 0],
        "Fatigue": [1, 1, 1, 1],
        "Difficulty Breathing": [0, 1, 0, 1],
        "Age": [45, 60, 38, 50],
        "Gender": ["Male", "Female", "Female", "Male"],
        "Blood Pressure": [140, 150, 135, 145],
        "Cholesterol Level": [210, 250, 190, 230],
        "Outcome Variable": [1, 1, 0, 1],
    }

    df = pd.DataFrame(data)

    st.subheader("Disease Count")
    disease_count = df["Disease"].value_counts().reset_index()
    disease_count.columns = ["Disease", "Count"]
    st.bar_chart(disease_count.set_index("Disease"))

    st.subheader("Cholesterol Level by Age")
    fig = px.scatter(df, x="Age", y="Cholesterol Level", color="Disease", size="Blood Pressure",
                     title="Cholesterol Level vs Age")
    st.plotly_chart(fig)

    st.subheader("Outcome Variable by Disease")
    outcome_avg = df.groupby("Disease")["Outcome Variable"].mean().reset_index()
    fig2 = px.bar(outcome_avg, x="Disease", y="Outcome Variable",
                  title="Average Outcome by Disease")
    st.plotly_chart(fig2)

    # AI-generated insight (optional placeholder)
    if st.button("Generate AI Insight"):
        insight = "Patient’s blood pressure shows slight elevation trend. Recommend monitoring weekly."
        st.info(insight)