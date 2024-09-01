from pydantic import BaseModel
import uuid
import datetime
from src.schemas.users import UserCreate

class BookingCreate(BaseModel):
    event_id: str
    user_id: str
    device_id: str
