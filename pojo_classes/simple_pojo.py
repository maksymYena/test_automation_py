from typing import List

from pydantic import BaseModel


class Support(BaseModel):
    url: str
    text: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersResponse(BaseModel):
    data: List[UserData]
    support: Support
