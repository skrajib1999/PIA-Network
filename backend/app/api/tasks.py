from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app.models import models
from app.api.deps import get_current_user, get_db
from app.schemas.task import TaskOut, TaskComplete

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Reward configuration
DEFAULT_TASK_REWARD = 5

@router.get("/", response_model=List[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.post("/complete")
def complete_task(
    data: TaskComplete,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    task = db.query(models.Task).filter(models.Task.id == data.task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    already_done = db.query(models.TaskCompletion).filter_by(
        task_id=task.id,
        user_id=current_user.id
    ).first()

    if already_done:
        raise HTTPException(status_code=400, detail="Task already completed")

    # Save completion
    completion = models.TaskCompletion(
        user_id=current_user.id,
        task_id=task.id,
        completed_at=datetime.utcnow()
    )
    db.add(completion)

    # Reward user
    current_user.balance += task.reward or DEFAULT_TASK_REWARD

    db.commit()

    return {"message": "Task completed successfully", "reward": task.reward, "new_balance": current_user.balance}
