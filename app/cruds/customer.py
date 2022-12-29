from sqlalchemy.orm import Session

from models.models import Customer
import schemas.customer as customer_schema

async def create_customer(
    db: Session, customer_create: customer_schema.CustomerCreate
) -> Customer:
    customer = Customer(**customer_create.dict())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

async def get_customers(db: Session):
    customers = db.query(Customer).all()
    return customers

async def get_customer(db: Session, customer_id: int) -> Customer:
  customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
  return customer if customer is not None else None

def delete_customer(db: Session, customer: Customer) -> None:
  db.delete(customer)
  db.commit()
  return customer.customer_id

def update_customer(db: Session, remarks: str, original: Customer) -> Customer:
  original.customer_remarks = remarks
  db.add(original)
  db.commit()
  db.refresh(original)
  return original


  



