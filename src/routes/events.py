from fastapi import APIRouter

from typing import List
from src.models.events import Event
from src.controllers.events import get_all_events

events_router = APIRouter()

@events_router.get("/all")
async def get_events() -> List[Event]:
    return get_all_events()