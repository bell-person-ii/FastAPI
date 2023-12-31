from fastapi import FastAPI,Body,HTTPException,Depends
from schema.request import AttendanceRequest
from sqlalchemy.orm import Session
from database.connection import get_db
from database.orm import Attendance
from schema.response import AttendanceSchema
from database.repository import create_Attendance

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/attendacnes/create",status_code= 201)
def createAttendance(request : AttendanceRequest, session: Session = Depends(get_db)):
    attendance = Attendance.create(request=request)
    attendance = create_Attendance(session= session, attendance = attendance)
    return AttendanceSchema.from_orm(attendance)

#우와 새해다~