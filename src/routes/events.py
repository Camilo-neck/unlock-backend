from fastapi import APIRouter, Request
from typing import List
from src.models.events import Event
import src.controllers.events as events
from src.utils.decorators import protected_route, public_route

events_router = APIRouter()

# Get all events of the admin-user
@events_router.get("/")
@protected_route()
async def get_admin_events(request: Request) -> List[Event]:
    return await events.get_admin_events(admin_id = request.state.user.id)