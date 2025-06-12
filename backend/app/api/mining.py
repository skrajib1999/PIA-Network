from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.models import User
from app.core.config import settings

router = APIRouter(prefix="/mining", tags=["Mining"])

# Set mining cooldown
MINING_COOLDOWN = timedelta(hours=12)
REWARD_AMOUNT = 10  # Example coin reward per session

@router.post("/mine")
def mine_now(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    now = datetime.utcnow()

    # Check last mined time
    if current_user.last_mined_at:
        time_since_last_mine = now - current_user.last_mined_at
        if time_since_last_mine < MINING_COOLDOWN:
            remaining = MINING_COOLDOWN - time_since_last_mine
            raise HTTPException(
                status_code=400,
                detail=f"Please wait {remaining.seconds // 3600}h {((remaining.seconds // 60) % 60)}m before mining again."
            )

    # Add reward
    current_user.balance += REWARD_AMOUNT
    current_user.last_mined_at = now

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Mining successful!",
        "reward": REWARD_AMOUNT,
        "new_balance": current_user.balance,
        "next_available_in": str(MINING_COOLDOWN)
    }
