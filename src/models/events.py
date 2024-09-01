from pydantic import BaseModel
import uuid

class Event(BaseModel):
    id: str
    admin_id: str
    name: str
    description: str
    location: str
    capacity: int
    start_time: str
    end_time: str
    created_at: str
