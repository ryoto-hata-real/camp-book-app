
from datetime import date

from pydantic import BaseModel, Field


class UserBase(BaseModel):
  client_email: str
  client_tel: str
  default_amount: int
  price: int

  class Config:
    orm_mode = True

class User(UserBase):
  client_id: str

class UserCreate(UserBase):
  pass

class UserCreateResponse(UserCreate):
  client_id: str

  class Config:
    orm_mode = True