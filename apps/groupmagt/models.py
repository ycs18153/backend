from array import array
from multiprocessing import managers
from typing import Optional, List
import uuid
from pydantic import BaseModel, Field


class groupModel(BaseModel):
    groupId: str = Field(default_factory=uuid.uuid4, alias="_id")  # 群組ID
    group_name: str = Field(...)  # 群組名稱
    state: bool = Field(...)
    group_managers: List[str] = Field(...)  # 群組管理員
    member_joined_message: str = Field(...)
    member_joined_figure: str = Field(...)
    leave_group_message: str = Field(...)  # 退群詞
    oil_switch: bool = Field()
    exchange_switch: bool = Field()
    weather_switch: bool = Field()
    zodiacSigns_switch: bool = Field()
    member_joined_message_switch: bool = Field()
    member_joined_figure_switch: bool = Field()
    signup_date: str = Field(...)  # 群組機器人註冊日期

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "groupId": "C8c55ed54b7107dd775c55b1483a7fef3",
                "group_name": "R",
                "state": 0,
                "group_managers": ["TWL"],
                "member_joined_message": "",
                "member_joined_figure": "",
                "leave_group_message": "",
                "oil_switch": 1,
                "exchange_switch": 1,
                "weather_switch": 1,
                "zodiacSigns_switch": 1,
                "member_joined_message_switch": 0,
                "member_joined_figure_switch": 0,
                "signup_date": "1995-12-12-12:12",
            }
        }


class authenticationCodeModel(BaseModel):
    code: str = Field(...)
    animal: str = Field(...)
    Enable: bool = Field(...)


class UpdateTaskModel(BaseModel):
    group_name: Optional[str]
    group_managers: Optional[List[str]]
    signup_date: Optional[str]
    black_list: Optional[List[str]]
    welcome_group_message: Optional[str]
    leave_group_message: Optional[str]
    no_flag_list: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "group_name": "",
                "group_managers": [""],
                "black_list": [],
                "welcome_group_message": "",
                "leave_group_message": "",
                "no_flag_list": [],
                "signup_date": "",
            }
        }
