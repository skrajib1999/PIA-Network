from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    avatar: Optional[HttpUrl] = None
    bio: Optional[str] = None
    balance: int
    is_admin: bool

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    avatar: Optional[HttpUrl] = None
    bio: Optional[str] = None


from pydantic import BaseModel, EmailStr, Field

from datetime import datetime

# Shared properties for user
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

# Properties to receive on user creation
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

# Properties to receive on user update
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6)
    is_active: Optional[bool] = None

# Properties to return via API (response model)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
