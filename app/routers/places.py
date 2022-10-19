from datetime import date
from sqlite3 import Date
from fastapi import APIRouter

router = APIRouter()


@router.get("/places/{client_id}", tags=["places"])
async def read_customers():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/places/{client_id}", tags=["places"])
async def read_customer(client_id: str, empty_amount: int, date: date):
    return {"username": "fakecurrentuser"}