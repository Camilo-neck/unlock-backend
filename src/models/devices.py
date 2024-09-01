from pydantic import BaseModel
import uuid

class Device(BaseModel):
    id: str
    event_id: str
    name: str
    status: str
    created_at: str