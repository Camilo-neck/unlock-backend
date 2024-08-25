from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.users import User
import src.controllers.users as users

users_router = APIRouter()

# Me
@users_router.get("/me")
@protected_route()
async def me(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    user_response = users.get_user()
    return User.from_response(user_response)

