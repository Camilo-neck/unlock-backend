from typing import List
import uuid
from src.supa.client import sb
from datetime import datetime
from fastapi import HTTPException
from enum import Enum
from src.models.access import Access, PopulatedAccess
from src.schemas.access import AccessCreate

from src.controllers.users import UserController
from src.controllers.devices import DeviceController

class AccessAction(str, Enum):
    enter = "enter"
    exit = "exit"

devices_table = sb.table("access")

class AccessController:

    @staticmethod
    def insert_access(access_create: AccessCreate) -> Access:
        # Query the most recent action for the same user, event, and device
        previous_access = devices_table.select("*").eq("user_id", access_create.user_id).eq("event_id", access_create.event_id).eq("device_id", access_create.device_id).order("access_at", desc=True).limit(1).execute()

        # Determine the next action based on the previous action
        if previous_access.data:
            last_action = previous_access.data[0]["action"]
            next_action = AccessAction.exit if last_action == AccessAction.enter else AccessAction.enter
        else:
            next_action = AccessAction.enter

        # Insert the new access record
        access = devices_table.insert({
            "access_at": datetime.now().isoformat(),
            "action": next_action,
            **access_create.dict()
        }).execute()

        return Access(**access.data[0])
    
    @staticmethod
    def get_accesses_by_event(event_id: str) -> List[Access]:
        accesses = devices_table.select("*").eq("event_id", event_id).execute()
        return [Access(**access) for access in accesses.data]
    
    @staticmethod
    def get_populated_accesses_by_event(event_id: str) -> List[PopulatedAccess]:
        accesses = devices_table.select("*").eq("event_id", event_id).execute()
        user_ids = [access["user_id"] for access in accesses.data]
        device_ids = [access["device_id"] for access in accesses.data]

        users = UserController.get_users_by_ids(user_ids)
        devices = DeviceController.get_devices_by_ids(device_ids)

        populated_accesses = []
        for access in accesses.data:
            user = next(user for user in users if user.id == access["user_id"])
            device = next(device for device in devices if device.id == access["device_id"])
            populated_accesses.append(PopulatedAccess(
                id=access["id"],
                user_email=user.email,
                device_name=device.name,
                action=access["action"],
                access_at=access["access_at"]
            ))

        return populated_accesses
    