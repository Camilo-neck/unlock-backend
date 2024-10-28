from pydantic import BaseModel

class AccessCreate(BaseModel):
    event_id: str
    user_id: str
    device_id: str