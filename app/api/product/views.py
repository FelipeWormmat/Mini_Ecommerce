from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from .schemas import ProductSchema, ShowProductSchema
from sqlalchemy.orm import Session
from app.api.services.auth_service import get_user, only_admin
from app.models.models import Product
from fastapi.exceptions import HTTPException
from app.api.repositories.product_repository import ProductRepository



router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
    repository.create(Product(**product.dict()))


@router.get('/', response_model=List[ShowProductSchema])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product: ProductSchema, repository: ProductRepository = Depends()):
    repository.update(id, product.dict())


@router.get('/{id}', response_model=ShowProductSchema)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)