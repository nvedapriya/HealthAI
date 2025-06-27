import streamlit as st
import sys, os
import uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chat import display_patient_chat
from disease_prediction import display_disease_prediction
from treatment_plan import display_treatment_plans
from analytics_dashboard import display_health_analytics
from profile_management import manage_patient_profile

# ✅ Set layout and theme
st.set_page_config(
    page_title="HealthAI - Intelligent Healthcare Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Sidebar Navigation (defined ONCE)
st.sidebar.title("🩺 Health AI Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Profile Management","Disease Prediction", "Treatment Plans", "Health Analytics", "Chat Assistant"],
    key="sidebar_navigation"
)

# ✅ Optional Styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        .stTextInput>div>input, .stTextArea textarea {
            background-color: #f1f1f1 !important;
            color: #000000 !important;
        }
        .stTextArea textarea {
            background-color: #ffffff !important;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

if page == "Profile Management":
    st.sidebar.markdown("## 🧑‍⚕️ Patient Profile")
    with st.sidebar.form(key=f"profile_sidebar_form_{uuid.uuid4()}"):
        name = st.text_input("Name", key="sidebar_profile_name")
        age = st.number_input("Age", min_value=0, step=1, key="sidebar_profile_age")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="sidebar_profile_gender")
        contact = st.text_input("Contact Number", key="sidebar_profile_contact")
        submitted = st.form_submit_button("Save")
        if submitted:
            st.sidebar.success(f"✅ Saved for {name}")


# ✅ Title (shown on all pages)
st.title("🩺 HealthAI - Intelligent Healthcare Assistant")
st.markdown("### 24/7 Patient Support")
st.markdown("Ask any health-related question for immediate assistance.")
st.markdown("---")

# ✅ Render Pages
try:
    if page == "Profile Management":
        st.success("Patient profile is editable in the sidebar.")  # ✅ Just this text

    elif page == "Disease Prediction":
        display_disease_prediction()

    elif page == "Treatment Plans":
        display_treatment_plans()

    elif page == "Health Analytics":
        display_health_analytics()

    elif page == "Chat Assistant":
        display_patient_chat()

except Exception as e:
    st.error(f"⚠ An error occurred while loading the feature: {e}")
