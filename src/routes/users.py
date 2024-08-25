from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials

from typing import List
import uuid
from gotrue.types import UserResponse
import src.controllers.users as users

from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route

users_router = APIRouter()

# Me
@users_router.get("/me")
@protected_route()
async def me(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserResponse:
    return await users.get_user()

