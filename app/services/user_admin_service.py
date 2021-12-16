from fastapi import Depends
from app.repositories.user_repository import UserRepository
from app.api.user_admin.schemas import AdminUserSchema
from app.api.user.schemas import UserSchema
from app.common.exceptions import EmailAdminUserAuthentication
from app.models.models import User
from typing import Union


class UsersAdminService:
    def __init__(self, users_repository: UserRepository = Depends()):
        self.users_repository = users_repository

    def unique_email(self, email: str):
        if self.users_repository.find_by_email(email):
            raise EmailAdminUserAuthentication()

    def create_user(self, users_admin: Union[AdminUserSchema, UserSchema]):
        self.unique_email(users_admin.email)
        return self.users_repository.create(User(**users_admin.dict()))
        

    def unique_email_update(self, email: str, id: int):
        query = self.users_repository.find_by_email(email)
        if query and query.id != id:
            raise EmailAdminUserAuthentication()

    def update(self, id: int, users_admin: Union[AdminUserSchema, UserSchema]):
        self.unique_email_update(users_admin.email, id)
        return self.users_repository.update(id, users_admin.dict())