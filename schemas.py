from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[int] = 1
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None


class Task(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
