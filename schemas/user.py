# create schema using Pydantic

from pydantic import BaseModel, EmailStr, Field

class UserIn(BaseModel):
    full_name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr 