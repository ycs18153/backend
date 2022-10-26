from array import array
from multiprocessing import managers
from typing import Optional, List
import uuid
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    groupId: str = Field(default_factory=uuid.uuid4, alias="_id")
    group_name: str = Field(...)
    group_managers: List[str] = Field(...)
    signup_date: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "groupId": "C8c55ed54b7107dd775c55b1483a7fef3",
                "group_name": "R",
                "group_managers": ["TWC"],
                "signup_date": "2022-10-20-20:10:00",
            }
        }


class UpdateTaskModel(BaseModel):
    group_name: Optional[str]
    managers: Optional[str]
    transcation_date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "My important task",
                "completed": True,
            }
        }
