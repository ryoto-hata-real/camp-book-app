from fastapi import APIRouter
import schemas.user as user_schema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.user as user_crud
from database import get_db

from datetime import date

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

@router.post('/user', response_model=user_schema.UserCreateResponse, tags=["users"])
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return await user_crud.create_user(db, user)