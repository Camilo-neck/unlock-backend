from typing import Optional
from pydantic import BaseModel
import uuid

class User(BaseModel):
    id: uuid.UUID
    email: str
    app_metadata: dict
    user_metadata: dict
    aud: str
    confirmation_sent_at: Optional[str]
    recovery_sent_at: Optional[str]
    email_change_sent_at: Optional[str]
    new_email: Optional[str]
    new_phone: Optional[str]
    invited_at: Optional[str]
    action_link: Optional[str]
    phone: Optional[str]
    created_at: str
    confirmed_at: Optional[str]
    email_confirmed_at: Optional[str]
    phone_confirmed_at: Optional[str]
    last_sign_in_at: Optional[str]
    role: str
    updated_at: str
    identities: list
    is_anonymous: bool
    factors: Optional[str]  # Make factors optional