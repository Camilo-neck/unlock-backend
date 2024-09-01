from typing import List
import uuid
from src.supa.client import sb
from fastapi import HTTPException

from src.models.events import Event
from src.schemas.events import EventCreate


events_table = sb.table("events")

class EventController:
    # Dependencies
    @staticmethod
    def verify_event_existence(event_id: str, admin_id: str) -> Event:
        event = EventController.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if str(event.admin_id) != admin_id:
            raise HTTPException(status_code=401, detail="Unauthorized to access requested event")
        return event 

    # Methods
    @staticmethod
    def get_admin_events(admin_id: str) -> List[Event]:
        events = events_table.select("*").eq("admin_id", admin_id).execute()
        return [Event(**event) for event in events.data]
    
    @staticmethod
    def get_participant_events(user_id: str) -> List[Event]:
        from src.controllers.bookings import BookingController
        bookings = BookingController.get_bookings_by_user(user_id)
        event_ids = [booking.event_id for booking in bookings]
        events = events_table.select("*").in_("id", event_ids).execute()
        return [Event(**event) for event in events.data]

    @staticmethod
    def create_event(event_create: EventCreate, admin_id: str) -> Event:
        event = events_table.insert({
            "admin_id": admin_id,
            **event_create.dict()
        }).execute()
        return Event(**event.data[0])

    @staticmethod
    def get_event_by_id(event_id: str) -> Event:
        event = events_table.select("*").eq("id", event_id).execute()
        return Event(**event.data[0]) if event.data else None

    @staticmethod
    def event_exists(event_id: str, admin_id: str) -> bool:
        return True if EventController.get_event_by_id(event_id) else False
    
    @staticmethod
    def update_event_capacity(event_id: str, capacity: int) -> Event:
        event = events_table.update({"capacity": capacity}).eq("id", event_id).execute()
        return Event(**event.data[0])