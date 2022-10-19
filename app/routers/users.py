from fastapi import APIRouter
import schemas.user as user_schema

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
async def create_user(user_info: user_schema.UserCreate):
    return user_schema.UserCreateResponse(client_id='aaaa',created_at=date.today(),  **user_info.dict())