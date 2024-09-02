from pydantic import BaseModel
import uuid
from datetime import datetime

from src.models.events import Event
from src.models.users import User
from src.models.devices import Device

from src.controllers.events import EventController
from src.controllers.users import UserController
from src.controllers.devices import DeviceController


class Booking(BaseModel):
    id: str
    event_id: str
    user_id: str
    device_id: str
    checked_in: bool
    created_at: datetime

class BookingPopulated(BaseModel):
    id: str
    event: Event
    device: Device
    user: User
    checked_in: bool
    created_at: datetime

    @classmethod
    def from_booking(cls, booking: Booking):
        event = EventController.get_event_by_id(booking.event_id)
        user = UserController.get_user_by_id(booking.user_id)
        device = DeviceController.get_device_by_id(booking.device_id)
        return cls(
            id=booking.id,
            event=event,
            user=user,
            device=device,
            checked_in=booking.checked_in,
            created_at=booking.created_at
        )