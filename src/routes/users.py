from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.users import User
from src.controllers.users import UserController
from src.schemas.users import UserCreate

users_router = APIRouter()

# Me
@users_router.get("/me")
@protected_route()
async def me(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    user = UserController.get_user_by_id(request.state.user.id)
    return user

@users_router.post("/create")
@protected_route()
async def create_user(user_create: UserCreate, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    return UserController.create_user(user_create, email_confirm=True)

# # Get user by id
# @users_router.get("/{user_id}")
# @protected_route()
# async def get_user_by_id(user_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
#     user = UserController.get_user_by_id(user_id)
#     return user