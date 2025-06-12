from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    reward: int

    class Config:
        orm_mode = True

class TaskComplete(BaseModel):
    task_id: int


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Base schema with shared fields
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    reward: float = Field(..., gt=0, description="Reward amount for completing the task")
    is_active: Optional[bool] = True

# Schema for creating a new task
class TaskCreate(TaskBase):
    pass

# Schema for updating an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    reward: Optional[float] = Field(None, gt=0)
    is_active: Optional[bool] = None

# Schema for returning task info via API
class TaskResponse(TaskBase):
    id: int
