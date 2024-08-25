from typing import List
import uuid
from src.supa.client import sb

from gotrue.types import UserResponse

async def get_user() -> UserResponse:
    user = sb.auth.get_user()
    return user