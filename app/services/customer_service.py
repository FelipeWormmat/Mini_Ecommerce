from fastapi import Depends
from app.api.user.schemas import UserSchema
from app.models.models import Customer
from app.services.user_service import UsersService
from app.repositories.custumer_repository import CustomerRepository
from app.api.customers.schemas import CustomersInsertSchema, CustomerSchema
from app.repositories.user_repository import UserRepository

class CustomersService:
    def __init__(self, users_service: UsersService = Depends(), customers_repository: CustomerRepository = Depends(), users_repository: UserRepository = Depends()) -> None:
        self.users_service = users_service
        self.customers_repository = customers_repository
        self.users_repository = users_repository

    def create(self, schema: CustomersInsertSchema):
        user_schema: UserSchema = schema.user
        user_schema.role = 'customer'
        self.users_service.create(user_schema)
        customer_schema: CustomerSchema = CustomerSchema(**schema.dict())
        customer = Customer(**customer_schema.dict())
        customer.user_id = self.users_repository.get_by_email(user_schema.email).id
        self.customers_repository.create(customer)