from src.supa.client import sb

class AuthController:
    @staticmethod
    def signin(email: str, password: str) -> dict:
        response = sb.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return response

    @staticmethod
    def signup(email: str, password: str) -> dict:
        response = sb.auth.sign_up({
            "email": email,
            "password": password
        })
        return response