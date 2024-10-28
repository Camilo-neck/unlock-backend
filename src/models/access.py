from pydantic import BaseModel
from datetime import datetime

class Access(BaseModel):
    id: str
    user_id : str
    event_id: str
    device_id: str
    access_at: str
    action: str

class PopulatedAccess(BaseModel):
    id: str
    user_email: str
    device_name: str
    action: str
    access_at: datetime