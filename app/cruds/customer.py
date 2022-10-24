from sqlalchemy.orm import Session

from models.models import Customer
import schemas.customer as customer_schema

async def create_customer(
    db: Session, customer_create: customer_schema.CustomerCreate
) -> Customer:
    customer = Customer(**customer_create.dict())
    print(customer)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer
