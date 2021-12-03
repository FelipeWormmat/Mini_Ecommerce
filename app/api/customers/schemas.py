from pydantic import BaseModel
from datetime import date, datetime

class CustomerSchema(BaseModel):
    birth_date: date
    document_id: int
    first_name: str
    genre: str
    last_name: str
    phone: str

class ShowCustomerSchema(CustomerSchema):
    id: int

    class Config:
        orm_mode = True
