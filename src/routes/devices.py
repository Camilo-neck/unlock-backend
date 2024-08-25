from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.devices import Device
from src.schemas.devices import DeviceCreate
import src.controllers.devices as devices

devices_router = APIRouter()

# Get device by id
@devices_router.get("/{device_id}")
@protected_route()
async def get_device_by_id(device_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Device:
    return devices.get_device_by_id(device_id)

# Get devices by event
@devices_router.get("/event/{event_id}")
@protected_route()
async def get_devices_by_event(event_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Device]:
    return devices.get_devices_by_event(event_id)

# Create a new device
@devices_router.post("/create")
@protected_route()
async def create_device(request: Request, device_create: DeviceCreate, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Device:
    return devices.create_device(device_create)