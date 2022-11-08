from fastapi import APIRouter
import schemas.user as user_schema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

import cruds.user as user_crud
from database import get_db

from datetime import date

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/{client_id}", tags=["users"])
async def read_user(client_id: int, db: Session = Depends(get_db)):
    return await user_crud.get_user(db, client_id)

@router.post('/user', response_model=user_schema.UserCreateResponse, tags=["users"])
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return await user_crud.create_user(db, user)


@router.put('/user/default/{client_id}', tags=['users'])
async def update_user_default(client_id: int, default_amount: Union[int, None] = None, price: Union[int, None] = None, db: Session = Depends(get_db)):
    user = await user_crud.get_user(db, client_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    update = await user_crud.update_user_default(db, user, default_amount, price)

    return update if update is not None else None


@router.put('/user/profile/{client_id}', tags=['users'])
async def update_user_profile(client_id: int, tel: Union[str, None] = None, email: Union[str, None] = None, db: Session = Depends(get_db)):
    user = await user_crud.get_user(db, client_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    update = await user_crud.update_user_profile(db, user, tel, email)

    return update if update is not None else None

@router.get('/user/customers/{client_id}', tags=["users"])
async def get_booked_users(client_id: int, db: Session = Depends(get_db), date: Union[date, None]=None):
    booked_users = await user_crud.get_booked_users(client_id, db, date)
    if booked_users is None:
        HTTPException(status_code=404, detail="Customers not found")
    return booked_users
