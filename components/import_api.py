import streamlit as st

from services.api_specification_service import ApiSpecificationService


def show_import_api_tab(project):

    st.subheader("📥 Import API Specification")

    uploaded_file = st.file_uploader(
        "Choose OpenAPI File",
        type=["json", "yaml", "yml"]
    )

    if uploaded_file:

        if st.button(
            "🚀 Upload Specification",
            use_container_width=True
        ):

            ApiSpecificationService.import_specification(
                project["id"],
                uploaded_file
            )

            st.success("Specification uploaded successfully!")

            st.rerun()

    specification = ApiSpecificationService.get_specification(
        project["id"]
    )

    if specification.data:

        spec = specification.data[0]

        st.divider()

        st.subheader("Current Specification")

        st.success("✅ Specification uploaded")

        st.write(f"**File:** {spec['file_name']}")
        st.write(f"**API Title:** {spec['api_title']}")
        st.write(f"**API Version:** {spec['api_version']}")
        st.write(f"**OpenAPI Version:** {spec['openapi_version']}")

    else:

        st.info("No specification uploaded yet.")