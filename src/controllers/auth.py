from src.supa.client import sb, init_supabase_client

class AuthController:
    # @staticmethod
    # def signin(email: str, password: str) -> dict:
    #     response = sb.auth.sign_in_with_password({
    #         "email": email,
    #         "password": password
    #     })
    #     return response

    # @staticmethod
    # def signup(email: str, password: str) -> dict:
    #     response = sb.auth.sign_up({
    #         "email": email,
    #         "password": password
    #     })
    #     return response
    
    @staticmethod
    def get_access_token(email: str, password: str) -> str:
        temp_sb = init_supabase_client()
        response = temp_sb.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        access_token = response.session.access_token
        return access_token
    