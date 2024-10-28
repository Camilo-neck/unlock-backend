from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.access import PopulatedAccess
from src.schemas.access import AccessCreate
from src.controllers.access import AccessController
from src.controllers.events import EventController

access_router = APIRouter()

@access_router.get("/event/{event_id}", response_model=List[PopulatedAccess])
@protected_route()
async def get_accesses_by_event(event_id: str, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    EventController.verify_event_existence(event_id, request.state.user.id)
    return AccessController.get_populated_accesses_by_event(event_id)