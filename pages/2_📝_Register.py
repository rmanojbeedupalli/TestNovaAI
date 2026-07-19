import streamlit as st
from services.auth_service import AuthService

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Account")

st.write("Create your TestNova AI account.")

with st.form("register_form"):

    email = st.text_input("Email Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    submit = st.form_submit_button("Register")

if submit:

    if not email or not password or not confirm_password:
        st.error("Please fill all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        try:

            AuthService.register(
                email=email,
                password=password
            )

            st.success("✅ Account created successfully!")

            st.info("You can now login.")

        except Exception as e:
            st.error(str(e))