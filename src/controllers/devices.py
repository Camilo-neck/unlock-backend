from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime
from fastapi import HTTPException

from src.models.devices import Device
from src.schemas.devices import DeviceCreate

from src.controllers.events import EventController

devices_table = sb.table("devices")
events_table = sb.table("events")

class DeviceController:
    # Dependencies
    @staticmethod
    def verify_device_existence(device_id: uuid.UUID, admin_id: uuid.UUID) -> Device:
        device = DeviceController.get_device_by_id(device_id)
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")
        EventController.verify_event_existence(device["event_id"], admin_id) #! Not sure if this is mandatory
        return device

    # Methods
    @staticmethod
    def get_device_by_id(device_id: uuid.UUID) -> Device:
        device = devices_table.select("*").eq("id", device_id).execute()
        return device.data[0] if device.data else None

    @staticmethod
    def get_devices_by_event(event_id: uuid.UUID) -> List[Device]:
        devices = devices_table.select("*").eq("event_id", event_id).execute()
        return devices.data

    #! At ths moment we cant create a device without an event
    @staticmethod
    def create_device(device_create: DeviceCreate, admin_id: uuid.UUID) -> Device:
        EventController.verify_event_existence(device_create.event_id, admin_id)

        device = devices_table.insert({
            "created_at": datetime.now().isoformat(),
            **device_create.dict()
        }).execute()
        return device.data[0]
    
    #TODO: Register device to event