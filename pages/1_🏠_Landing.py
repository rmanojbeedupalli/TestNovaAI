import streamlit as st

st.set_page_config(
    page_title="TestNova AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 TestNova AI")

st.subheader("Autonomous API Quality Engineering Platform")

st.markdown("---")

st.write("""
Welcome to **TestNova AI**, an intelligent platform that helps QA engineers
automatically generate API test cases, create test data, execute API tests,
analyze failures, and generate professional reports using Generative AI.
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/2_📝_Register.py")

with col2:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/3_🔐_Login.py")