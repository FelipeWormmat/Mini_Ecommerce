from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.api.product_discount.schemas import ProductDiscountSchema, ShowProductDiscountSchema

from app.db.db import get_db
from app.models.models import ProductDiscount

router = APIRouter()

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(db: Session = Depends(get_db)):
    return db.query(ProductDiscount).all()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, db: Session = Depends(get_db)):
    db.add(ProductDiscount(**product_discount.dict()))
    db.commit()

@router.get('/{id}', response_model=ShowProductDiscountSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(ProductDiscount).filter_by(id = id).first()

@router.put('/{id}')
def update(id: int, product_discount: ProductDiscountSchema, db: Session = Depends(get_db)):
    query = db.query(ProductDiscount).filter_by(id=id)
    query.update(product_discount.dict())
    db.commit()