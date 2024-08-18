from typing import List
from src._supabase.supabase_client import supabase_client as sb

from src.models.events import Event
from src.schemas.events import EventCreate

def get_all_events() -> List[Event]:
    events = sb.from_("events").select("*").execute()
    return events.data