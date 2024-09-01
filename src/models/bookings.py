from pydantic import BaseModel
import uuid
from datetime import datetime

class Booking(BaseModel):
    id: str
    event_id: str
    user_id: str
    device_id: str
    checked_in: bool
    created_at: datetime
