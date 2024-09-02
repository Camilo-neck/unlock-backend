from src.supa.client import init_supabase_client

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
        #We use a temporary client to get the access token to avoid overwriting the main client
        response = init_supabase_client().auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        access_token = response.session.access_token
        return access_token
    