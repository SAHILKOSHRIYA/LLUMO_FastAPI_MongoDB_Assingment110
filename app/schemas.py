from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date, datetime

class EmployeeBase(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    joining_date: Optional[date] = None
    skills: Optional[List[str]] = None

    @validator("skills", pre=True, always=False)
    def empty_skills_to_list(cls, v):
        if v is None:
            return v
        return list(v)

class EmployeeCreate(EmployeeBase):
    employee_id: str = Field(..., min_length=1)
    name: str
    department: str
    salary: float
    joining_date: date
    skills: List[str]

class EmployeeUpdate(EmployeeBase):
   
    pass

class EmployeeOut(BaseModel):
    employee_id: str
    name: str
    department: str
    salary: float
    joining_date: datetime
    skills: List[str]



class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str