from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime

from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate

bookings_table = sb.table("bookings")

def get_booking_by_id(booking_id: uuid.UUID) -> Booking:
    booking = bookings_table.select("*").eq("id", booking_id).execute()
    return booking.data[0] if booking.data else None

def get_bookings_by_user(user_id : uuid.UUID) -> List[Booking]:
    bookings = bookings_table.select("*").eq("user_id", user_id).execute()
    return bookings.data

def get_bookings_by_event(event_id : uuid.UUID) -> List[Booking]:
    bookings = bookings_table.select("*").eq("event_id", event_id).execute()
    return bookings.data

def get_bookings_by_device(device_id : uuid.UUID) -> List[Booking]:
    bookings = bookings_table.select("*").eq("device_id", device_id).execute()
    return bookings.data

def create_booking(booking_create: BookingCreate) -> Booking:
    booking = bookings_table.insert({
        "booked_at": datetime.now(),
        "checked_in": False,
        **booking_create.dict()
    }).execute()
    return booking.data[0]
