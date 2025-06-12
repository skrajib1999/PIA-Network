from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Wallet info schema
class WalletInfo(BaseModel):
    user_id: int
    balance: float = Field(..., ge=0, description="Current wallet balance")
    currency: str = Field(default="PIA", description="Crypto token symbol")

# Transaction record schema
class TransactionRecord(BaseModel):
    id: int
    user_id: int
    amount: float
    transaction_type: str  # e.g., "deposit", "withdrawal", "reward"
    timestamp: datetime
    status: str  # e.g., "pending", "completed", "failed"

    class Config:
        orm_mode = True

# Optional: Request to create a withdrawal
class WithdrawalRequest(BaseModel):
    user_id: int
    amount: float = Field(..., gt=0, description="Amount to withdraw")
    wallet_address: str
