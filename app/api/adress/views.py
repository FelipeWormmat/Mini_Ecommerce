from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from app.models.models import Address
from app.repositories.adress_repository import AddressRepository
from app.api.adress.schemas import AdressSchema, ShowAdressSchema
from app.services.adress_service import AddressService

router = APIRouter()

@router.get('/', response_model=List[ShowAdressSchema])
def index(repository: AddressRepository = Depends()):
    return repository.get_all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(address: AdressSchema, service: AddressService = Depends()):
    service.create(address)

@router.get('/{id}', response_model=ShowAdressSchema)
def show(id: int, repository: AddressRepository = Depends()):
    return repository.get_by_id(id)

@router.put('/{id}')
def update(id: int, address: AdressSchema,  service: AddressService = Depends()):
    service.update(id, address)

@router.delete('/{id}')
def delete(id: int, repository: AddressRepository = Depends()):
    repository.delete(id)