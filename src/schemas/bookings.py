from pydantic import BaseModel
import uuid
import datetime

class BookingCreate(BaseModel):
    event_id: str
    user_id: str
    device_id: str