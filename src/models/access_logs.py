from pydantic import BaseModel
import uuid

class AccessLog(BaseModel):
    id: uuid.UUID
    device_id: uuid.UUID
    user_id: uuid.UUID
    event_id: uuid.UUID
    access_at: str
    action: str