from pydantic import BaseModel


class AdminUserSchema(BaseModel):
    display_name: str
    email: str
    role = "admin"
    password: str


class ShowAdminUserSchema(BaseModel):
    display_name: str
    email: str
    role = "admin"
    id: int

    class Config:
        orm_mode = True


class ShowAdminUsersSchema(AdminUserSchema):
    id: int

    class Config:
        orm_mode = True