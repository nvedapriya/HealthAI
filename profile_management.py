import streamlit as st
import uuid  # To generate unique form keys

def manage_patient_profile():
    st.subheader("🧑‍⚕️ Patient Profile")

    form_key = f"manage_patient_profile_form_{uuid.uuid4()}"  # 🔑 Unique form key

    with st.form(key=form_key):
        name = st.text_input("Name", key="profile_name")
        age = st.number_input("Age", min_value=0, step=1, key="profile_age")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="profile_gender")
        contact = st.text_input("Contact Number", key="profile_contact")

        submitted = st.form_submit_button("Save", type="primary", use_container_width=True)

        if submitted:
            st.success(f"Profile saved for {name}")
