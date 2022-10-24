from datetime import date
from pydantic import BaseModel

class CustomerBase(BaseModel):
  client_id: int
  booked_date: date
  customer_number: int
  customer_name: str
  customer_tel: str
  customer_email: str
  customer_remarks: str

  class Config:
    orm_mode = True
  

class Customer(CustomerBase):
  customer_id: int

class CustomerCreate(CustomerBase):
  pass

class CustomerCreateResponse(CustomerCreate):
  customer_id: int

  class Config:
    orm_mode = True