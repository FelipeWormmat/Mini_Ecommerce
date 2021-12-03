from pydantic import BaseModel
from datetime import date, datetime

class AdressSchema(BaseModel):
    birth_date: date
    document_id: int
    first_name: str
    genre: str
    last_name: str
    phone: str

class ShowAdressSchema(AdressSchema):
    id: int

    class Config:
        orm_mode = True
