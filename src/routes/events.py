from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials

from typing import List
from src.models.events import Event
from src.schemas.events import EventCreate
import src.controllers.events as events

from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route

events_router = APIRouter()

# Create a new event
@events_router.post("/create")
@protected_route()
async def create_event(request: Request, event_create: EventCreate, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Event:
    return await events.create_event(event_create, admin_id = request.state.user.id)

# Get all events of the admin-user
@events_router.get("/")
@protected_route()
async def get_admin_events(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Event]:
    return await events.get_admin_events(admin_id = request.state.user.id)