
from datetime import date

from pydantic import BaseModel, Field


class UserBase(BaseModel):
  client_email: str
  client_tel: str
  default_amount: int
  price: str

  class Config:
    orm_mode = True

class User(UserBase):
  client_id: str
  created_at: date
    

class UserCreate(UserBase):
  pass

class UserCreateResponse(UserCreate):
  client_id: str
  created_at: date

  class Config:
    orm_mode = True