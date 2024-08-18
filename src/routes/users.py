from fastapi import APIRouter

from typing import List
from src.models.users import User
from src.controllers.users import get_all_users

users_router = APIRouter()

@users_router.get("/all")
async def get_users() -> List[User]:
    return get_all_users()