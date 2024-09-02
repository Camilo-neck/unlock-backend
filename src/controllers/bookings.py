from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime
from fastapi import HTTPException
import random
from gotrue.errors import AuthApiError

from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate
from src.schemas.users import UserCreate

from src.controllers.events import EventController
from src.controllers.devices import DeviceController
from src.controllers.users import UserController

bookings_table = sb.table("bookings")

class BookingController:
    # Dpendencies
    @staticmethod
    def verify_booking_existence(booking_id: str, admin_id: str) -> Booking:
        booking = BookingController.get_booking_by_id(booking_id)
        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        # Check if user is admin of the booking's event
        EventController.verify_event_existence(booking.event_id, admin_id)
        return booking
    
    # Methods
    @staticmethod
    def get_booking_by_id(booking_id: str) -> Booking:
        booking = bookings_table.select("*").eq("id", booking_id).execute()
        return Booking(**booking.data[0]) if booking.data else None

    @staticmethod
    def get_bookings_by_user(user_id: str) -> List[Booking]:
        bookings = bookings_table.select("*").eq("user_id", user_id).execute()
        return [Booking(**booking) for booking in bookings.data]

    @staticmethod
    def get_bookings_by_event(event_id: str) -> List[Booking]:
        bookings = bookings_table.select("*").eq("event_id", event_id).execute()
        return [Booking(**booking) for booking in bookings.data]

    @staticmethod
    def get_bookings_by_device(device_id: str) -> List[Booking]:
        bookings = bookings_table.select("*").eq("device_id", device_id).execute()
        return [Booking(**booking) for booking in bookings.data]

    @staticmethod
    def create_booking(booking_create: BookingCreate) -> Booking:
        # Discount capacity from event
        booking_create_event_id = booking_create.event_id

        event = EventController.get_event_by_id(booking_create_event_id)
        event_capacity = event.capacity
        if event_capacity <= 0:
            raise HTTPException(status_code=400, detail="Event is full")
        
        event = EventController.update_event_capacity(event.id, event_capacity - 1)

        booking = bookings_table.insert({
            "created_at": datetime.now().isoformat(),
            "checked_in": False,
            **booking_create.dict()
        }).execute()
        return Booking(**booking.data[0])
    
    @staticmethod
    def create_bookings_and_users(event_id : str, user_create_list = list[UserCreate]) -> List[Booking]:
        booking_create_event_id = event_id
        booking_create_users = user_create_list

        # Check event capacity
        event = EventController.get_event_by_id(booking_create_event_id)
        event_capacity = event.capacity
        if event_capacity < len(booking_create_users):
            raise HTTPException(status_code=400, detail=f"Not enough capacity for event [Capacity: {event_capacity}, Users: {len(booking_create_users)}]")

        # First we need to create the users if they don't exist
        users = []
        for user_create in booking_create_users:
            try:
                user = UserController.create_user(user_create, password="Unlock@123", email_confirm=False) #TODO: Send email and user create_user_and_send_verification_email
            except AuthApiError as e:
                user = UserController.get_user_by_email(user_create.email)
                if not user:
                    raise HTTPException(status_code=400, detail=f"Error creating user {user_create.email}, Error: {e}")
            users.append(user)
        
        # Get all devices
        devices = DeviceController.get_devices_by_event(booking_create_event_id)
        device_ids = [device.id for device in devices]

        # Then we create the bookings
        # We assign random devices to the users
        bookings = []
        for user in users:
            skip_booking = False
            user_bookings = BookingController.get_bookings_by_user(user.id)
            for booking in user_bookings:
                if str(booking.event_id) == str(booking_create_event_id):
                    print(f"User {user.id} already has a booking for event {booking_create_event_id}")
                    skip_booking = True
                    bookings.append(booking)
                    break  # Exit the loop as we found an existing booking

            if not skip_booking:
                device_id = random.choice(device_ids)
                booking = BookingController.create_booking(BookingCreate( #TODO: Send email to user with booking info
                    event_id=booking_create_event_id,
                    user_id=user.id,
                    device_id=str(device_id)
                ))
                bookings.append(booking)

        return bookings
    

