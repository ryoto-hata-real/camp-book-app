from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas.customer as customer_schema
import cruds.customer as customer_crud
from database import get_db

router = APIRouter()


@router.get("/customers/", tags=["customers"])
async def read_customers():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/customer/{customer_id}", tags=["customers"])
async def read_customer(customer_id: str):
    return {"username": "fakecurrentuser"}


@router.post("/customer/", response_model=customer_schema.CustomerCreateResponse, tags=["customers"])
async def create_customer(customer: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    return await customer_crud.create_customer(db, customer)
    
