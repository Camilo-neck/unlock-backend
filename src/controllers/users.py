from typing import List
import uuid
from src.supa.client import sb

from gotrue.types import UserResponse
from src.models.users import User
from src.schemas.users import UserCreate

class UserController:

    @staticmethod
    def get_user_by_id(user_id: str) -> User:
        user_response = sb.auth.admin.get_user_by_id(user_id)
        return User.from_response(user_response)
    
    @staticmethod
    def get_users_by_ids(user_ids: List[str]) -> List[User]:
        users_response = sb.auth.admin.list_users()
        return [User.from_response(user) for user in users_response if user.id in user_ids]
    
    @staticmethod
    def get_user_by_email(email: str) -> User:
        users_response = sb.auth.admin.list_users()
        for user in users_response:
            if user.email == email:
                return User.from_response(user)
        return None
    
    @staticmethod
    def list_users() -> List[User]:
        users_response = sb.auth.admin.list_users()
        return [User.from_response(user) for user in users_response]
    
    @staticmethod
    def create_user(user_create: UserCreate, password: str, email_confirm: bool) -> User:
        user_response = sb.auth.admin.create_user({
            'email': user_create.email,
            'password': password, # Temporary password
            'phone': user_create.phone,
            'email_confirm': email_confirm,
            'options': {
                'data': {
                    'full_name': user_create.full_name,
                    'age': user_create.age
                }
            },
        })
        
        return User.from_response(user_response)
    
    @staticmethod
    def create_user_and_send_verification_email(user_create: UserCreate) -> User:
        user_response = sb.auth.sign_in_with_otp({
            'email': user_create.email,
            'phone': user_create.phone,
            'options': {
                'should_create_user': True,
                'data': {
                    'full_name': user_create.full_name,
                    'age': user_create.age
                }
            },
        })
        
        return User.from_response(user_response)