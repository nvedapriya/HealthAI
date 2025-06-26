import streamlit as st
from granite_model import generate_treatment_plan

def display_treatment_plans(model=None):
    st.subheader("Personalized Treatment Planner")

    condition = st.text_input("Enter diagnosis or condition:")
    if st.button("Generate Treatment Plan") and condition:
        plan = generate_treatment_plan(condition)
        st.markdown("### Recommended Treatment:")
        st.markdown(plan)
