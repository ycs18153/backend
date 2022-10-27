from array import array
from multiprocessing import managers
from typing import Optional, List
import uuid
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    groupId: str = Field(default_factory=uuid.uuid4, alias="_id")  # 群組ID
    group_name: str = Field(...)  # 群組名稱
    group_managers: List[str] = Field(...)  # 群組管理員
    black_list: List[str] = Field(...)  # 黑名單 (必須放 user_id, not user_name)
    welcome_group_message: str = Field(...)  # 入群歡迎詞
    leave_group_message: str = Field(...)  # 退群詞
    no_flag_list: List[str] = Field(...)  # 不標記名單
    signup_date: str = Field(...)  # 群組機器人註冊日期

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "groupId": "C8c55ed54b7107dd775c55b1483a7fef3",
                "group_name": "R",
                "group_managers": ["TWC"],
                "black_list": [],
                "welcome_group_message": "Welcome!",
                "leave_group_message": "Goodbye!",
                "no_flag_list": [],
                "signup_date": "2022-10-20-20:10:00",
            }
        }


class UpdateTaskModel(BaseModel):
    group_name: Optional[str]
    group_managers: Optional[str]
    signup_date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "My important task",
                "completed": True,
            }
        }
