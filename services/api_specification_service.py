import os
import json
import yaml

from services.supabase_service import supabase


class ApiSpecificationService:

    @staticmethod
    def extract_metadata(uploaded_file):
        """
        Extract OpenAPI metadata from JSON or YAML file.
        """

        filename = uploaded_file.name.lower()

        content = uploaded_file.getvalue()

        if filename.endswith(".json"):
            data = json.loads(content.decode("utf-8"))

        else:
            data = yaml.safe_load(content)

        return {
            "openapi_version": data.get("openapi", ""),
            "api_title": data.get("info", {}).get("title", ""),
            "api_version": data.get("info", {}).get("version", "")
        }

    @staticmethod
    def upload_specification(project_id, uploaded_file):
        """
        Upload specification to Supabase Storage.
        """

        storage_path = f"{project_id}/{uploaded_file.name}"

        supabase.storage.from_("api-specifications").upload(
            storage_path,
            uploaded_file.getvalue()
        )

        return storage_path

    @staticmethod
    def save_metadata(
        project_id,
        uploaded_file,
        storage_path,
        metadata
    ):

        return supabase.table("specifications").insert({

            "project_id": project_id,

            "file_name": uploaded_file.name,

            "storage_path": storage_path,

            "file_type": os.path.splitext(
                uploaded_file.name
            )[1].replace(".", ""),

            "openapi_version": metadata["openapi_version"],

            "api_title": metadata["api_title"],

            "api_version": metadata["api_version"]

        }).execute()
    
    @staticmethod
    def import_specification(project_id, uploaded_file):
            """
            Complete workflow for importing an API specification.
            """
            metadata = ApiSpecificationService.extract_metadata(
            uploaded_file
        )

            storage_path = ApiSpecificationService.upload_specification(
            project_id,
            uploaded_file
        )

            ApiSpecificationService.save_metadata(
            project_id,
            uploaded_file,
            storage_path,
            metadata
        )

            return metadata
    
    @staticmethod
    def get_specification(project_id):

        return (
            supabase.table("specifications")
            .select("*")
            .eq("project_id", project_id)
            .limit(1)
            .execute()
        )