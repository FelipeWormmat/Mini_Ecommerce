from os import name
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String, TinyInteger
from app.db.db import Base

class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)

class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Supplier(Base):

    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class PaymentMethods(Base):

    __tablename__ = 'paymentmethods'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    enabled = Column(TinyInteger())