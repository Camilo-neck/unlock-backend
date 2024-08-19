from typing import List
from src.supa.client import sb

from src.models.events import Event
from src.schemas.events import EventCreate

async def get_admin_events(admin_id: str) -> List[Event]:
    events = sb.table("events").select("*").eq("admin_id", admin_id).execute()
    return events.data

async def create_event(event_create: EventCreate, admin_id: str) -> Event:
    event = sb.table("events").insert({
        "admin_id": admin_id,
        **event_create.dict()
    }).execute()
    return event.data[0]