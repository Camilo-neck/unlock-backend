from pydantic import BaseModel
import uuid

class User(BaseModel):
    id: uuid.UUID
    email: str
    password: str
    first_name: str
    last_name: str
    created_at: str
    updated_at: str
    last_login: str
    role: str
    status: str