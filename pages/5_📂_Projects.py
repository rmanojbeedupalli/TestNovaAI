import streamlit as st

from services.project_service import ProjectService
from utils.auth_utils import (
    require_login,
    get_current_user,
    set_active_project,
    get_active_project
)

st.set_page_config(
    page_title="Projects",
    page_icon="📂"
)

require_login()


# -----------------------------
# Create Project
# -----------------------------
def create_project_dialog():

    with st.expander("➕ Create New Project"):

        with st.form("create_project"):

            project_name = st.text_input("Project Name", key="project_name")
            description = st.text_area("Description", key="project_description")

            submit = st.form_submit_button("🚀 Create Project",use_container_width=True)

            if submit:

                if not project_name.strip():
                    st.error("Project name is required.")

                else:

                    user = get_current_user()

                    try:

                        ProjectService.create_project(
                            user.id,
                            project_name,
                            description
                        )

                        # Clear form values
                        st.session_state.pop("project_name", None)
                        st.session_state.pop("project_description", None)

                        # Set success flag
                        st.session_state["project_created"] = (f'✅ Project "{project_name}" created successfully!')

                        st.rerun()

                    except Exception as e:

                        st.error(str(e))


# -----------------------------
# Project List
# -----------------------------
def show_project_list():
  
    st.title("📂 Projects")

    if "project_created" in st.session_state:

        st.success(st.session_state["project_created"])

        del st.session_state["project_created"]

    create_project_dialog()

    st.divider()

    st.subheader("My Projects")

    user = get_current_user()

    projects = ProjectService.get_projects(user.id)

    if len(projects.data) == 0:

        st.info("No projects created yet.")

        return

    for project in projects.data:

        col1, col2 = st.columns([5, 1])

        with col1:

            st.markdown(f"### 📁 {project['project_name']}")
            st.caption(project["description"])

        with col2:

            if st.button(
                "Open",
                key=project["id"]
            ):

                set_active_project(project)

                st.rerun()

        st.divider()


# -----------------------------
# Workspace
# -----------------------------
def show_project_workspace():

    project = get_active_project()

    if not project:

        st.warning("No active project selected.")
        return

    if st.button("← Back to Projects"):

        st.session_state.pop("active_project", None)

        st.rerun()

    st.title(f"📁 {project['project_name']}")

    st.caption(project["description"])

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1️⃣ Import API",
        "2️⃣ Explore API",
        "3️⃣ Generate Tests",
        "4️⃣ Run Tests",
        "5️⃣ Results & Reports"
    ])

    with tab1:
        st.info("Import API module will be implemented next.")

    with tab2:
        st.info("Explore API module coming soon.")

    with tab3:
        st.info("AI Test Generator coming soon.")

    with tab4:
        st.info("Test Execution coming soon.")

    with tab5:
        st.info("Reports module coming soon.")


# -----------------------------
# Main
# -----------------------------
active_project = get_active_project()

if active_project:
    show_project_workspace()
else:
    show_project_list()