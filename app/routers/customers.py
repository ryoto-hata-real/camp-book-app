from fastapi import APIRouter

router = APIRouter()


@router.get("/customers/", tags=["customers"])
async def read_customers():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/customer/{customer_id}", tags=["customers"])
async def read_customer(customer_id: str):
    return {"username": "fakecurrentuser"}
