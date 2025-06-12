from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Request to start mining or check status
class MiningStartRequest(BaseModel):
    user_id: int
    # Optional: specify mining power or settings
    mining_power: Optional[float] = Field(default=1.0, gt=0)

# Response with current mining status
class MiningStatusResponse(BaseModel):
    user_id: int
    total_mined: float = Field(..., description="Total crypto mined so far")
    last_mining_time: Optional[datetime] = None
    mining_power: float = Field(..., description="Current mining power")
    next_mining_available_at: Optional[datetime] = None

# Optional: mining reward or payout info
class MiningRewardResponse(BaseModel):
    user_id: int
    reward_amount: float
    rewarded_at: datetime
