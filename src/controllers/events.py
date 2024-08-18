from typing import List
from src.supa.client import sb

from src.models.events import Event
from src.schemas.events import EventCreate

async def get_admin_events(admin_id: str) -> List[Event]:
    events = sb.from_("events").select("*").eq("admin_id", admin_id).execute()
    return events.data