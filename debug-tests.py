from typing import List
from src.controllers.auth import AuthController
from src.controllers.users import UserController
from src.controllers.events import EventController
from src.controllers.devices import DeviceController
from src.controllers.bookings import BookingController
from src.controllers.access import AccessController
from src.core.config import settings

from src.schemas.users import UserCreate

user_create_list: List[UserCreate] = [
    UserCreate(
        email="jorozcove@unal.edu.co",
        full_name="Juan Orozco",
        phone="36416318",
        age=20
    ),
    UserCreate(
        email="ccuello+email1@unal.edu.co",
        full_name="Camilo Cuello",
        phone="6154916517",
        age=21
    )
]

response = BookingController.create_bookings_and_users(
    event_id="d270215d-c791-40fa-b281-d81ebfa42715",
    user_create_list=user_create_list
)

# # response = BookingController.get_populated_bookings_by_event("f2676266-c030-4d5e-b2a0-058ee93db610")

# # response = AccessController.get_populated_accesses_by_event("01a31646-d81e-4f90-aebd-bbb7efa54089")


print(response)
