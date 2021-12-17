from pydantic import BaseModel
from datetime import date, datetime
from app.api.user.schemas import UserSchema

class CustomerSchema(BaseModel):
    birth_date: date
    document_id: int
    first_name: str
    genre: str
    last_name: str
    phone: str

class ShowCustomerSchema(CustomerSchema):
    id: int

class CustomersInsertSchema(CustomerSchema):
    user: UserSchema

class UpdateCustumerSchema(CustomerSchema):
    first_name: str
    last_name: str
    phone_number: str
    birth_date: date
    genre: str
    
    class Config:
        orm_mode = True
