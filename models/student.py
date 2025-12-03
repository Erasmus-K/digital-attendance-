from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    admission_no = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)

    course_id = Column(Integer)

    attendance = relationship("Attendance", back_populates="student")
