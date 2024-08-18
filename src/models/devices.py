from pydantic import BaseModel
import uuid

class Device(BaseModel):
    id: uuid.UUID
    event_id: uuid.UUID
    name: str
    status: str
    created_at: str