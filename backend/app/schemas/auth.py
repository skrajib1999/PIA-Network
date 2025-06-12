from pydantic import BaseModel, EmailStr
from typing import Optional

# User login request schema
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Token response schema (e.g., JWT access token)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Token payload (decoded JWT data)
class TokenPayload(BaseModel):
    sub: Optional[str] = None  # user identifier (usually user id or email)
    exp: Optional[int] = None  # expiration timestamp

# Password reset request (optional)
class PasswordResetRequest(BaseModel):
    email: EmailStr

# Password change request (optional)
class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str
