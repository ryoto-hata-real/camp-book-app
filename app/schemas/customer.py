from datetime import date
from pydantic import BaseModel

class CustomerBase(BaseModel):
  client_id: str
  booked_date: date
  customer_number: int
  customer_name: str
  customer_tel: str
  customer_email: str
  customer_remarks: str

  class Config:
    orm_mode = True
  

class Customer(CustomerBase):
  customer_id: str
  created_at: date
  daleted_at: date

class CustomerCreate(CustomerBase):
  pass

class CustomerCreateResponse(CustomerCreate):
  customer_id: str
  created_at: date

  class Config:
    orm_mode = True