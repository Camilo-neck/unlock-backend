from src.supa.client import sb

# Login
def singin(email: str, password: str) -> dict:
    response = sb.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    return response

# Signup
def signup(email: str, password: str) -> dict:
    response = sb.auth.sign_up({
        "email": email,
        "password": password
    })
    return response