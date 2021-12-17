from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from app.services.customer_service import CustomersService
from app.models.models import Customer
from app.repositories.custumer_repository import CustomerRepository
from app.api.customers.schemas import CustomersInsertSchema, CustomerSchema, ShowCustomerSchema, UpdateCustumerSchema

router = APIRouter()

@router.get('/', response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(customer: CustomersInsertSchema, service: CustomersService = Depends()):
    service.create(customer)

@router.get('/{id}', response_model=ShowCustomerSchema)
def show(id: int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)

@router.put('/{id}')
def update(id: int, customer: UpdateCustumerSchema, repository: CustomerRepository = Depends()):
    repository.update(id, customer.dict())