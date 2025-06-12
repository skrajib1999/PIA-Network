from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Base referral data
class ReferralBase(BaseModel):
    referrer_id: int
    referred_email: EmailStr

# Create a referral request
class ReferralCreate(ReferralBase):
    pass

# Referral response schema
class ReferralResponse(ReferralBase):
    id: int
    created_at: datetime
    reward_earned: Optional[float] = 0.0

    class Config:
        orm_mode = True
