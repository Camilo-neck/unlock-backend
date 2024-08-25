from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime

from src.models.devices import Device
from src.schemas.devices import DeviceCreate

devices_table = sb.table("devices")

def get_device_by_id(device_id: uuid.UUID) -> Device:
    device = devices_table.select("*").eq("id", device_id).execute()
    return device.data[0] if device.data else None

def get_devices_by_event(event_id: uuid.UUID) -> List[Device]:
    devices = devices_table.select("*").eq("event_id", event_id).execute()
    return devices.data

def create_device(device_create: DeviceCreate) -> Device:
    device = devices_table.insert({
        "created_at": datetime.now(),
        **device_create.dict()
    }).execute()
    return device.data[0]