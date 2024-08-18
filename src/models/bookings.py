from pydantic import BaseModel
import uuid

class Booking(BaseModel):
    id: uuid.UUID
    event_id: uuid.UUID
    user_id: uuid.UUID
    device_id: uuid.UUID
    checked_in: bool
    booked_at: str
    created_at: str