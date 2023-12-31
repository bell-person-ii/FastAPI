from pydantic import BaseModel

class AttendanceRequest(BaseModel):
    count: int