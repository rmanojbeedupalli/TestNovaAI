import streamlit as st
from utils.auth_utils import require_login
from services.auth_service import AuthService
from utils.auth_utils import logout_user

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊"
)

require_login()

col1, col2 = st.columns([6, 1])

with col1:
    st.title("📊 Dashboard")

with col2:
    if st.button("Logout"):
        AuthService.logout()
        logout_user()
        st.success("Logged out successfully.")
        st.switch_page("pages/1_🏠_Landing.py")
st.success("Welcome to TestNova AI!")