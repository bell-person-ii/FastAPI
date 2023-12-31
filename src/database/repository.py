from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.orm import Attendance

def create_Attendance(session: Session, attendance: Attendance):
    session.add(instance=attendance)
    session.commit()
    session.refresh(instance=attendance)
    return attendance