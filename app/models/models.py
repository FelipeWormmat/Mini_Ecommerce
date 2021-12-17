from fastapi.security import base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float, Integer, String
from app.db.db import Base
from sqlalchemy import Column


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    #category = relationship(Category)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    #supplier = relationship(Supplier)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class PaymentMethods(Base):
    __tablename__ = 'paymentmethods'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    enabled = Column(Boolean())

class ProductDiscount(Base):
    __tablename__ = 'productdiscounts'

    id = Column(Integer, primary_key=True)
    value = Column(Float(10,2))
    payment_method_id = Column(Integer)
    product_id = Column(Integer, ForeignKey(Product.id))
    mode = Column(String(45))
    product = relationship(Product)
    payment_method_id = Column(Integer, ForeignKey(PaymentMethods.id))
    payment_method = relationship(PaymentMethods)

class Coupons(Base):
    __tablename__ = 'coupons'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(DateTime)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customer)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    display_name = Column(String(100))
    email = Column(String(50))
    role = Column(String(10))
    password = Column(String(100))

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    number = Column(String(10))
    status = Column(String(15))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customer)
    created_at = Column(DateTime)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    total_value = Column(Float(10,2))
    payment_form_id = Column(Integer)
    total_discount = Column(Float(10,2))

class OrderStatus(Base):
    __tablename__ = 'order_statuses'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship(Order)
    status = Column(String(15))
    created_at = Column(DateTime)

class OrderProducts(Base):
    __tablename__ = 'order_products'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship(Order)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)
    quantity = Column(Integer)