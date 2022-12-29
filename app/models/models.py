from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
  __tablename__ = 'users'

  client_id = Column(Integer, primary_key=True, autoincrement=True)
  client_tel = Column(String(256), nullable=False)
  client_email = Column(String(256), nullable=False)
  client_name = Column(String(256), nullable=True)
  default_amount = Column(Integer)
  price = Column(Integer)

  relationship("Customer", back_populates="user")


class Customer(Base):
  __tablename__ = 'customers'

  customer_id = Column(Integer, primary_key=True)
  client_id = Column(Integer, ForeignKey("users.client_id"), nullable=False)
  booked_date = Column(Date, nullable=False)
  customer_number = Column(Integer, nullable=False)
  customer_name = Column(String, nullable=False)
  customer_tel = Column(String, nullable=False)
  customer_email = Column(String)
  customer_remarks = Column(String)

  relationship("User", back_populates="customers")

class Place(Base):
  __tablename__ = 'places'

  client_id = Column(Integer, ForeignKey("users.client_id"), primary_key=True)
  empty_amount = Column(Integer, nullable=False)
  date = Column(Date)

  relationship("User", back_populates="places")


  


  
