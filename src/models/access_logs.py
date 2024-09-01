from pydantic import BaseModel
import uuid

class AccessLog(BaseModel):
    id: str
    device_id: str
    user_id: str
    event_id: str
    access_at: str
    action: str