from typing import List
import uuid
import resend
import secrets
import string
from src.supa.client import sb
from src.core.config import settings

from gotrue.types import UserResponse
from src.models.users import User
from src.schemas.users import UserCreate

resend.api_key = settings.resend_key

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
        users_response = UserController.list_users()
        for user in users_response:
            if user.email == email:
                return User.from_response(user)
        return None
    
    @staticmethod
    def list_users() -> List[User]:
        users = []
        page = 1
        per_page = 100
    
        while True:
            users_response = sb.auth.admin.list_users(page=page, per_page=per_page)
            if not users_response:
                break
            users.extend(User.from_response(user) for user in users_response)
            page += 1
    
        return users
    
    @staticmethod
    def create_user(user_create: UserCreate, email_confirm: bool, event_name: str = None) -> User:
        password = UserController.generate_password(15)
        user_response = sb.auth.admin.create_user({
            'email': user_create.email,
            'password': password,
            'phone': user_create.phone,
            'email_confirm': email_confirm,
            'options': {
                'data': {
                    'full_name': user_create.full_name,
                    'age': user_create.age
                }
            },
        })

        UserController.send_account_created_email(user_create.email, password, event_name) 
        return User.from_response(user_response)
    
    @staticmethod
    def send_account_created_email(email: str, password: str, event_name: str = None) -> None:
        params = {
            "from" : f"unlock team <{settings.from_email}>",
            "to": email,
            "subject": "Unlock - Account created",
            "html": f'''<html>
                <body>
                    <h1>An Unlock account has been created for you</h1>
                    {f'<p>You have been added to the event: <strong>{event_name}</strong></p>' if event_name else ''}
                    <p>Your email is: <strong>{email}</strong></p>
                    <p>Your temporary password is: <strong>{password}</strong></p>
                    <p>Log in {settings.movil_url}/login to access your events!</p>
                    <p>Log in {settings.web_url}/login to administrate your own events</p>
                </body>
            </html>'''
        }
        resend.Emails.send(params)

    @staticmethod
    def send_event_added_email(email: str, event_name: str) -> None:
        params = {
            "from" : f"unlock team <{settings.from_email}>",
            "to": email,
            "subject": "Unlock - Event added",
            "html": f'''<html>
                <body>
                    <h1>You have been added to the event: {event_name}</h1>
                    <p>Log in {settings.movil_url}/login to access your events!</p>
                    <p>Log in {settings.web_url}/login to administrate your own events</p>
                </body>
            </html>'''
        }
        resend.Emails.send(params)
        
    @staticmethod
    def generate_password(length: int) -> str:
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password
    
    # @staticmethod
    # def create_user_and_send_verification_email(user_create: UserCreate) -> User:
    #     user_response = sb.auth.sign_in_with_otp({
    #         'email': user_create.email,
    #         'phone': user_create.phone,
    #         'options': {
    #             'should_create_user': True,
    #             'email_redirect_to': f"{settings.web_url}/dashboard",
    #             'data': {
    #                 'full_name': user_create.full_name,
    #                 'age': user_create.age
    #             }
    #         },
    #     })
        
    #     return User.from_response(user_response)
    
    # @staticmethod
    # def invite_user(user_create: UserCreate) -> User:
    #     user_response = sb.auth.admin.invite_user_by_email(
    #         email = user_create.email,
    #         options = {
    #             'data': {
    #                 'full_name': user_create.full_name,
    #                 'age': user_create.age
    #             },
    #             'redirect_to': f"{settings.web_url}/dashboard"
    #         })

    #     return User.from_response(user_response)