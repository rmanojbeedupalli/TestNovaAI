from services.supabase_service import supabase


class AuthService:

    @staticmethod
    def register(email, password):
        """Register a new user"""
        return supabase.auth.sign_up({
            "email": email,
            "password": password
        })

    @staticmethod
    def login(email, password):
        """Login existing user"""
        return supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

    @staticmethod
    def logout():
        """Logout current user"""
        return supabase.auth.sign_out()