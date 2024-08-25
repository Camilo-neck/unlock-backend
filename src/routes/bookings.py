from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate
import src.controllers.bookings as bookings

bookings_router = APIRouter()

# Get booking by id
@bookings_router.get("/{booking_id}")
@protected_route()
async def get_booking_by_id(booking_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Booking:
    return bookings.get_booking_by_id(booking_id)

# Get my bookings
@bookings_router.get("/me")
@protected_route()
async def get_my_bookings(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    return bookings.get_bookings_by_user(request.state.user.id)

# Get bookings by user
@bookings_router.get("/user/{user_id}")
@protected_route()
async def get_bookings_by_user(user_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    return bookings.get_bookings_by_user(user_id)

# Get bookings by event
@bookings_router.get("/event/{event_id}")
@protected_route()
async def get_bookings_by_event(event_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    return bookings.get_bookings_by_event(event_id)

# Get bookings by device
@bookings_router.get("/device/{device_id}")
@protected_route()
async def get_bookings_by_device(device_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Booking]:
    return bookings.get_bookings_by_device(device_id)

# Create a new booking
@bookings_router.post("/create")
@protected_route()
async def create_booking(request: Request, booking_create: BookingCreate, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Booking:
    return bookings.create_booking(booking_create)