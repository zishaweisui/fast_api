from typing import List
from pydantic import BaseModel
from datetime import datetime

class BaseNote(BaseModel):
    id: int | None
    user_id: int | None
    content: str
    created_date: datetime | None
    updated_date: datetime | None

class BaseUser(BaseModel):
    id: int | None
    fname: str
    lname: str
    created_date: datetime | None
    updated_date: datetime | None
    notes: List[BaseNote] = [] 
