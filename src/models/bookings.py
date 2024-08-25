from pydantic import BaseModel
import uuid
from datetime import datetime

class Booking(BaseModel):
    id: uuid.UUID
    event_id: uuid.UUID
    user_id: uuid.UUID
    device_id: uuid.UUID
    booked_at: datetime
    checked_in: bool
    created_at: datetime
