from services.supabase_service import supabase


class AuthService:
    """Handles user authentication using Supabase."""

    @staticmethod
    def register(email: str, password: str):
        """Register a new user."""
        return supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )

    @staticmethod
    def login(email: str, password: str):
        """Authenticate an existing user."""
        return supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

    @staticmethod
    def logout():
        """Logout current user."""
        supabase.auth.sign_out()