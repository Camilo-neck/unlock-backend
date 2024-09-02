import uuid
from typing import List
from datetime import datetime
from pydantic import BaseModel
from gotrue.types import UserResponse, UserIdentity

class User(BaseModel):
    id: str
    email: str
    phone: str
    app_metadata: dict
    user_metadata: dict
    # confirmed_at: datetime
    role: str
    created_at: datetime
    updated_at: datetime
    # identities: List[UserIdentity]

    @classmethod
    def from_response(cls, response: UserResponse) -> "User":
        #check if response has user property
        if hasattr(response, "user"):
            return cls(
                id=response.user.id,
                email=response.user.email,
                phone=response.user.phone,
                app_metadata=response.user.app_metadata,
                user_metadata=response.user.user_metadata,
                # confirmed_at=response.user.confirmed_at,
                role=response.user.role,
                created_at=response.user.created_at,
                updated_at=response.user.updated_at,
            )
        
        return cls(
            id=response.id,
            email=response.email,
            phone=response.phone,
            app_metadata=response.app_metadata,
            user_metadata=response.user_metadata,
            # confirmed_at=response.confirmed_at,
            role=response.role,
            created_at=response.created_at,
            updated_at=response.updated_at,
        )