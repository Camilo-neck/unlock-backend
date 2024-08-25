from typing import List
import uuid
from src.supa.client import sb

from src.models.events import Event
from src.schemas.events import EventCreate

async def get_admin_events(admin_id: uuid.UUID) -> List[Event]:
    events = sb.table("events").select("*").eq("admin_id", admin_id).execute()
    return events.data

async def create_event(event_create: EventCreate, admin_id: uuid.UUID) -> Event:
    event = sb.table("events").insert({
        "admin_id": admin_id,
        **event_create.dict()
    }).execute()
    return event.data[0]

async def get_event_by_id(event_id: uuid.UUID, admin_id: uuid.UUID) -> Event:
    event = sb.table("events").select("*").eq("id", event_id).eq("admin_id", admin_id).execute()
    return event.data[0] if event.data else None

