from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from app.api.adress.schemas import AdressSchema, ShowAdressSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Address


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(adress: AdressSchema, db: Session = Depends(get_db)): 
    db.add(Address(**adress.dict())) 
    db.commit()


@router.get('/', response_model=List[ShowAdressSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Address).all()


@router.put('/{id}')
def update(id: int, adress: AdressSchema, db: Session = Depends(get_db)):
    query = db.query(Address).filter_by(id=id) 
    query.update(adress.dict())
    db.commit()


@router.get('/{id}', response_model=ShowAdressSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Address).filter_by(id=id).first()