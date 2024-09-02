from supabase import create_client, Client
from src.core.config import settings

class SupabaseClient:
    _instance = None
    _client: Client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseClient, cls).__new__(cls)
            cls._client = init_supabase_client()

        return cls._instance
    @property
    def client(self):
        return self._client   


def init_supabase_client():
    return create_client(settings.supabase_url, settings.supabase_service_role_key)   

sb = SupabaseClient().client