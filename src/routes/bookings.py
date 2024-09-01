from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate 
from src.controllers.bookings import BookingController

from src.controllers.events import EventController
from src.controllers.devices import DeviceController
from src.schemas.users import UserCreate

bookings_router = APIRouter()

# Get my bookings
@bookings_router.get("/me")
@protected_route()
async def get_my_bookings(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    return BookingController.get_bookings_by_user(request.state.user.id)

# Get booking by id
@bookings_router.get("/{booking_id}")
@protected_route()
async def get_booking_by_id(booking_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Booking:
    return BookingController.verify_booking_existence(booking_id, request.state.user.id)

# Get bookings by user
# @bookings_router.get("/user/{user_id}")
# @protected_route()
# async def get_bookings_by_user(user_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
#     return BookingController.get_bookings_by_user(user_id)

# Get bookings by device
# @bookings_router.get("/device/{device_id}")
# @protected_route()
# async def get_bookings_by_device(device_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
#     return BookingController.get_bookings_by_device(device_id)

# Get bookings by event
@bookings_router.get("/event/{event_id}")
@protected_route()
async def get_bookings_by_event(event_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    EventController.verify_event_existence(event_id, request.state.user.id)
    return BookingController.get_bookings_by_event(event_id)

# Create a new booking
@bookings_router.post("/create")
@protected_route()
async def create_booking(booking_create: BookingCreate, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Booking:
    DeviceController.verify_device_existence(booking_create.device_id, request.state.user.id)
    return BookingController.create_booking(booking_create)

# Create bookings and users
@bookings_router.post("/create_from_users/{event_id}")
@protected_route()
async def create_bookings_and_users(event_id: str, users_create_list : list[UserCreate], request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    EventController.verify_event_existence(event_id, request.state.user.id)
    return BookingController.create_bookings_and_users(event_id, users_create_list) 