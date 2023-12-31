from typing import List
from pydantic import BaseModel
from datetime import datetime

class AttendanceSchema(BaseModel):
    id : int
    time : datetime
    count : int

    class Config:
        from_attributes = True