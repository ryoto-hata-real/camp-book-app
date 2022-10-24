from datetime import date
from pydantic import BaseModel

class Place(BaseModel):
  client_id: int
  empty_amount: int
  date: date