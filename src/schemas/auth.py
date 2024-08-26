from pydantic import BaseModel

class Singup(BaseModel):
    email: str
    password: str

class Signin(BaseModel):
    email: str
    password: str

