import streamlit as st

from utils.auth_utils import (
    require_login,
    get_active_project
)

st.set_page_config(
    page_title="Project Workspace",
    page_icon="📁"
)

require_login()

project = get_active_project()

if not project:

    st.warning("Please select a project first.")

    if st.button("Go to Projects"):

        st.switch_page(
            "pages/5_📂_Projects.py"
        )

    st.stop()

st.title("📁 Project Workspace")

st.subheader(project["project_name"])

st.write(project["description"])

st.divider()

st.subheader("API Specification")

st.info(
    "No OpenAPI specification uploaded yet."
)

st.divider()

st.subheader("Endpoints")

st.info(
    "Endpoints will appear here."
)

st.divider()

st.subheader("AI Test Cases")

st.info(
    "Generated test cases will appear here."
)

st.divider()

st.subheader("Execution")

st.info(
    "Execution results will appear here."
)

st.divider()

st.subheader("Reports")

st.info(
    "Reports will appear here."
)