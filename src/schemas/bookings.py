from pydantic import BaseModel
import uuid
import datetime

class BookingCreate(BaseModel):
    event_id: uuid.UUID
    user_id: uuid.UUID
    device_id: uuid.UUID