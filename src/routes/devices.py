from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.models.devices import Device
from src.schemas.devices import DeviceCreate
from src.controllers.devices import DeviceController

devices_router = APIRouter()

# Get device by id
@devices_router.get("/{device_id}")
@protected_route()
async def get_device_by_id(device_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Device:
    return DeviceController.verify_device_existence(device_id, request.state.user.id)

# Get devices by event
@devices_router.get("/event/{event_id}")
@protected_route()
async def get_devices_by_event(event_id: uuid.UUID, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> List[Device]:
    return DeviceController.get_devices_by_event(event_id)

# Create a new device
@devices_router.post("/create")
@protected_route()
async def create_device(device_create: DeviceCreate, request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> Device:
    return DeviceController.create_device(device_create, request.state.user.id)