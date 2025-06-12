from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app import models, schemas
from app.core.config import settings


# --- USER CRUD ---

def create_user(db: Session, telegram_id: int, ref_code: str = None) -> models.User:
    user = db.query(models.User).filter(models.User.telegram_id == telegram_id).first()
    if user:
        return user

    new_user = models.User(
        telegram_id=telegram_id,
        balance=0,
        last_mined=datetime.utcnow() - timedelta(hours=settings.MINING_INTERVAL_HOURS)
    )

    # Handle referral
    if ref_code:
        referrer = db.query(models.User).filter(models.User.telegram_id == ref_code).first()
        if referrer:
            referrer.balance += settings.REFERRAL_REWARD
            new_user.referred_by = referrer.id

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_telegram_id(db: Session, telegram_id: int) -> models.User:
    return db.query(models.User).filter(models.User.telegram_id == telegram_id).first()


def update_user_balance(db: Session, user: models.User, amount: int):
    user.balance += amount
    db.commit()


# --- MINING ---

def can_mine(user: models.User) -> bool:
    return datetime.utcnow() - user.last_mined >= timedelta(hours=settings.MINING_INTERVAL_HOURS)


def mine_coin(db: Session, user: models.User) -> int:
    if not can_mine(user):
        raise HTTPException(status_code=400, detail="⛏️ Please wait before mining again.")

    reward = settings.DEFAULT_REWARD
    user.balance += reward
    user.last_mined = datetime.utcnow()
    db.commit()
    return reward


# --- TASKS ---

def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    new_task = models.Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_all_tasks(db: Session):
    return db.query(models.Task).all()


def complete_task(db: Session, user: models.User, task_id: int):
    existing = db.query(models.UserTask).filter_by(user_id=user.id, task_id=task_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Task already completed.")

    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")

    user_task = models.UserTask(user_id=user.id, task_id=task.id)
    user.balance += task.reward
    db.add(user_task)
    db.commit()


# --- LEADERBOARD ---

def get_top_miners(db: Session, limit: int = 10):
    return db.query(models.User).order_by(models.User.balance.desc()).limit(limit).all()
