from typing import List
from fastapi import APIRouter, status
from fastapi import Depends
from app.models.models import Product
from app.services.auth_service import only_admin
from .schemas import ProductSchema, ShowProductSchema
from app.repositories.product_repository import ProductRepository

router = APIRouter() 

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
    
    repository.create(Product(**product.dict()))

@router.get('/', response_model=List[ShowProductSchema]) 
def index(db: ProductRepository = Depends()):
    return db.get_all()

@router.put('/{id}')
def update(id: int, product: ProductSchema, repository: ProductRepository = Depends()):
    repository.update(id, product.dict())

@router.get('/{id}', response_model=ShowProductSchema)
def show(id:int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)