from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Unlock - Backend"
    debug: bool = False
    supabase_url: str
    supabase_key: str
    supabase_db_password: str
    supabase_service_role_key: str

    class Config:
        env_file = ".env"

settings = Settings()