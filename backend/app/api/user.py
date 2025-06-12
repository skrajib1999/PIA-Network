from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.models import User
from app.schemas.user import UserOut, UserUpdate
from app.api.deps import get_current_user, get_current_admin
from app.core.base import get_db

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/me", response_model=UserOut)
def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserOut)
def update_my_profile(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(current_user, key, value)

    db.commit()
    db.refresh(current_user)
    return current_user

@router.get("/balance")
def get_my_balance(current_user: User = Depends(get_current_user)):
    return {"balance": current_user.balance}

@router.get("/all", response_model=List[UserOut])
def list_all_users(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin)
):
    return db.query(User).all()
