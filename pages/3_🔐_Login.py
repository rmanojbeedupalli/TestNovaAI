import streamlit as st

from services.auth_service import AuthService
from utils.auth_utils import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered",
)

st.title("🔐 Login")

with st.form("login_form"):

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password",
    )

    submit = st.form_submit_button("Login")

if submit:

    if not email or not password:
        st.error("Please enter email and password.")

    else:

        try:

            response = AuthService.login(
                email,
                password,
            )

            login_user(response.user)

            st.success("Login Successful!")

            st.switch_page("pages/4_📊_Dashboard.py")

        except Exception as e:
            st.error(str(e))