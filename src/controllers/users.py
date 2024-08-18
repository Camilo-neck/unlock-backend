from typing import List
from src._supabase.supabase_client import supabase_client as sb

from src.models.users import User

def get_all_users() -> List[User]:
    return