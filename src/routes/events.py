from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.events import Event
from src.schemas.events import EventCreate
from src.controllers.events import EventController

events_router = APIRouter()

# Create a new event
@events_router.post("/create")
@protected_route()
async def create_event(request: Request, event_create: EventCreate, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Event:
    return EventController.create_event(event_create, request.state.user.id)

# Get all events of the admin-user
@events_router.get("/admin")
@protected_route()
async def get_admin_events(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Event]:
    return EventController.get_admin_events(request.state.user.id)

# Get all events of the participant-user
@events_router.get("/participant")
@protected_route()
async def get_participant_events(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Event]:
    return EventController.get_participant_events(request.state.user.id)

# Get event by id
@events_router.get("/{event_id}")
@protected_route()
async def get_event_by_id(event_id : str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Event:
    return EventController.verify_event_existence(event_id, request.state.user.id)