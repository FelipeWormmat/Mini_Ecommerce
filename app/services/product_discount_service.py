from fastapi import Depends
from app.api.product_discount.schemas import ProductDiscountSchema
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository

class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountSchema):
        pass