from fastapi import Request, HTTPException
from fastapi.security.utils import get_authorization_scheme_param
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from supabase import Client

class CustomAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, supabase: Client):
        super().__init__(app)
        self.supabase = supabase

    def dispatch(self, request: Request, call_next):
        authorization: str = request.headers.get("Authorization")
        scheme, token = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            request.state.user = None
        else:
            user_response = self.supabase.auth.get_user(token)
            if user_response is None:
                request.state.user = None
            else:
                request.state.user = user_response.user

        response = call_next(request)
        return response
