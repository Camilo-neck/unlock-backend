from pydantic import BaseModel

class EventCreate(BaseModel):
    admin_id: int
    name: str
    description: str
    location: str
    capacity: int
    start_time: str
    end_time: str