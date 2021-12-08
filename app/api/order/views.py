from fastapi import APIRouter, status, Depends
from app.api.order.schemas import OrderSchema
from app.models.models import User
from app.services.auth_service import get_user, only_admin
from app.services.order_service import OrderService

router = APIRouter(dependencies=[Depends(get_user)])

@router.post('/')
def create(input_order_schema: OrderSchema, service: OrderService = Depends(), user : User = Depends(get_user)):
    service.create(input_order_schema, user)