from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime
from fastapi import HTTPException

from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate

from src.controllers.events import EventController
from src.controllers.devices import DeviceController

bookings_table = sb.table("bookings")

class BookingController:
    # Dpendencies
    @staticmethod
    def verify_booking_existence(booking_id: uuid.UUID, admin_id: uuid.UUID) -> Booking:
        booking = BookingController.get_booking_by_id(booking_id)
        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        # Check if user is admin of the booking's event
        EventController.verify_event_existence(booking["event_id"], admin_id)
        return booking
    
    # Methods
    @staticmethod
    def get_booking_by_id(booking_id: uuid.UUID) -> Booking:
        booking = bookings_table.select("*").eq("id", booking_id).execute()
        return booking.data[0] if booking.data else None

    @staticmethod
    def get_bookings_by_user(user_id: uuid.UUID) -> List[Booking]:
        bookings = bookings_table.select("*").eq("user_id", user_id).execute()
        print(bookings.data)
        return bookings.data

    @staticmethod
    def get_bookings_by_event(event_id: uuid.UUID) -> List[Booking]:
        bookings = bookings_table.select("*").eq("event_id", event_id).execute()
        return bookings.data

    @staticmethod
    def get_bookings_by_device(device_id: uuid.UUID) -> List[Booking]:
        bookings = bookings_table.select("*").eq("device_id", device_id).execute()
        return bookings.data

    @staticmethod
    def create_booking(booking_create: BookingCreate) -> Booking:
        # EventController.verify_event_existence(booking_create["event_id"], admin_id)
        # Discount capacity from event
        event = EventController.get_event_by_id(booking_create.event_id)
        event_capacity = event["capacity"]
        if event_capacity <= 0:
            raise HTTPException(status_code=400, detail="Event is full")
        
        event = EventController.update_event_capacity(event["id"], event_capacity - 1)

        booking = bookings_table.insert({
            "created_at": datetime.now().isoformat(),
            "checked_in": False,
            **booking_create.dict()
        }).execute()
        return booking.data[0]