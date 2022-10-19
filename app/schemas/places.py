from datetime import date
from pydantic import BaseModel

class Place(BaseModel):
  client_id: str
  empty_amount: int
  date: date