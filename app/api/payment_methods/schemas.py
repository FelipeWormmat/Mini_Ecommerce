from pydantic import BaseModel


class PaymentSchema(BaseModel):
    enabled: int
    name: str


class ShowPaymentSchema(PaymentSchema):
    id: int
    
    class Config:
        orm_mode = True