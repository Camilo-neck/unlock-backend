from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.users import User
from src.controllers.users import UserController

users_router = APIRouter()

# Me
@users_router.get("/me")
@protected_route()
async def me(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    user_response = UserController.get_user()
    return User.from_response(user_response)

# Get user by id
@users_router.get("/{user_id}")
@protected_route()
async def get_user_by_id(user_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    user_response = UserController.get_user_by_id(user_id)
    return User.from_response(user_response)