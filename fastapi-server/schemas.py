from typing import List, Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str = Field(description="邮箱")


class UserCreate(UserBase):
    password: str = Field(description="密码")


class User(UserBase):
    id: int = Field(description="用户Id")
    is_active: bool = Field(description="是否启用")
    items: List[Item] = []

    class Config:
        orm_mode = True