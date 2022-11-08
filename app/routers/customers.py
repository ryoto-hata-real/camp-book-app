from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas.customer as customer_schema
import cruds.customer as customer_crud
from database import get_db

router = APIRouter()

@router.post("/customer/", response_model=customer_schema.CustomerCreateResponse, tags=["customers"])
async def create_customer(customer: customer_schema.CustomerCreate, db: Session = Depends(get_db)):
    return await customer_crud.create_customer(db, customer)


@router.get("/customer/{customer_id}", tags=["customers"])
async def read_customer(customer_id: str, db: Session = Depends(get_db)):
    return await customer_crud.get_customer(db, customer_id)


@router.delete("/customer/{customer_id}", tags=['customers'])
async def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = await customer_crud.get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    delete = customer_crud.delete_customer(db, customer)
    if delete:
        return delete
    else:
        return {"message": "Cannot Delete Customer"}

@router.put('/customer/{customer_id}', tags=["customers"])
async def update_customer(customer_id: str, remarks: str, db: Session = Depends(get_db)):
    customer = await customer_crud.get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    update = customer_crud.update_customer(db, remarks, customer)
    if update:
        return update
    else:
        return {"message": "Cannot UPdate Customer"}


    
