from services.supabase_service import supabase


class ProjectService:
    """Handles CRUD operations for Projects."""

    @staticmethod
    def create_project(user_id, project_name, description=""):
        """
        Create a new project.
        """

        response = (
            supabase.table("projects")
            .insert(
                {
                    "user_id": user_id,
                    "project_name": project_name,
                    "description": description,
                }
            )
            .execute()
        )

        return response

    @staticmethod
    def get_projects(user_id):
        """
        Get all projects belonging to a user.
        """

        response = (
            supabase.table("projects")
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response

    @staticmethod
    def delete_project(project_id):
        """
        Delete a project.
        """

        response = (
            supabase.table("projects")
            .delete()
            .eq("id", project_id)
            .execute()
        )

        return response