from sqlalchemy.orm import Session

import datetime
import models.models as models
import schemas.user as user_schema
import schemas.customer as customer_schema
from typing import Union

from datetime import date


async def create_user(
    db: Session, user_create: user_schema.UserCreate
) -> models.User:
    user = models.User(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_user(db:Session, client_id: int) -> models.User:
  user = db.query(models.User).filter(models.User.client_id == client_id).first()
  return user

async def update_user_default(db: Session, user: models.User, default_amount: Union[int, None] = None ,price: Union[int, None] = None) -> models.User:
  if default_amount is not None:
    user.default_amount = default_amount
  if price is not None:
    user.price = price
  db.commit()
  db.refresh(user)
  return user


async def update_user_profile(db: Session, user: models.User, tel: Union[str, None] = None, email: Union[str, None] = None) -> models.User:
  if tel is not None:
    user.client_tel = tel
  if email is not None:
    user.client_email = email
  db.commit()
  db.refresh(user)
  return user

async def get_booked_users(client_id:int , db: Session, date: date):
  if date is not None:
    users = db.query(models.Customer). \
      filter(models.Customer.client_id == client_id). \
        filter(models.Customer.booked_date > datetime.date.today()). \
          order_by(models.Customer.booked_date).all()
  else:
    users = db.query(models.Customer). \
      filter(models.Customer.client_id == client_id). \
        filter(models.Customer.booked_date == datetime.date.today()). \
          order_by(models.Customer.booked_date).all()
  
  return users