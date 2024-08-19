from pydantic import BaseModel

class Singup(BaseModel):
    email: str
    password: str

class Singin(BaseModel):
    email: str
    password: str

