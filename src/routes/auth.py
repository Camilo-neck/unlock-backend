from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordRequestForm
from src.core.auth_scheme import auth_scheme
from src.utils.decorators import protected_route, public_route
from typing import List
import uuid

from src.schemas.auth import Singin, Singup
import src.controllers.auth as auth

auth_router = APIRouter()

# Signin
@auth_router.post("/signin")
@public_route()
async def signin(request: Request, singin: Singin):
    return auth.singin(singin.email, singin.password)

# Signup
@auth_router.post("/signup")
@public_route()
async def signup(request: Request, singup: Singup):
    return auth.signup(singup.email, singup.password)

# Set token
@auth_router.post("/token")
@public_route()
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    reponse = auth.singin(form_data.username, form_data.password)
    return {"access_token": reponse.session.access_token, "token_type": "bearer"}