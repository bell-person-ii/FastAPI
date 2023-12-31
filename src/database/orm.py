from sqlalchemy import Boolean,Column,Integer,String,DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import mysql
from schema.request import AttendanceRequest
from datetime import datetime

Base = declarative_base()

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(mysql.INTEGER,primary_key=True,index=True)
    time = Column(DateTime,default=datetime.now())
    count = Column(mysql.INTEGER,nullable=False)

    def __repr__(self):
        return f"Attendance(id = {self.id}), time = {self.time}, count = {self.count}"


    @classmethod
    def create (cls, request: AttendanceRequest):
        return cls(count = request.count)



