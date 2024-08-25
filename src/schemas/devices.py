from pydantic import BaseModel

class DeviceCreate(BaseModel):
    event_id: str
    name: str
    status: str