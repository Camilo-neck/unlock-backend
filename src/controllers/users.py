from typing import List
from src.supa.client import sb

from src.models.users import User

def get_all_users() -> List[User]:
    return