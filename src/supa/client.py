from supabase import create_client, Client
from src.core.config import settings

url: str = settings.supabase_url
# key: str = settings.supabase_key
key: str = settings.supabase_service_role_key

def init_supabase_client():
    global sb
    sb = create_client(url, key)
    return sb

sb: Client = init_supabase_client()