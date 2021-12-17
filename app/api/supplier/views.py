from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.api.supplier.schemas import ShowSupplierSchema, SupplierSchema
from app.db.db import get_db
from app.models.models import Product, Supplier
from app.repositories.supplier_repository import SupplierRepository
from app.services.auth_service import only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))


@router.get('/', response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.update(id, supplier.dict())


@router.get('/{id}', response_model=ShowSupplierSchema)
def show(id: int, repository: SupplierRepository = Depends()):
    return repository.get_by_id(id=id)