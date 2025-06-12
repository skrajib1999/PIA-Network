class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    reward = Column(Integer, default=5)

class TaskCompletion(Base):
    __tablename__ = "task_completions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    completed_at = Column(DateTime, default=datetime.utcnow)






from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship
from app.core.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    username = Column(String, nullable=True)

    balance = Column(Integer, default=0)
    is_premium = Column(Boolean, default=False)
    referred_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    last_mined = Column(DateTime, server_default=func.now())

    created_at = Column(DateTime, server_default=func.now())

    referrals = relationship("User", remote_side=[id])
    tasks = relationship("UserTask", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    reward = Column(Integer, default=5)
    link = Column(String, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    user_tasks = relationship("UserTask", back_populates="task")


class UserTask(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))

    completed_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="tasks")
    task = relationship("Task", back_populates="user_tasks")
