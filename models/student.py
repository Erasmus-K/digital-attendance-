from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    admission_no = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)

    course_id = Column(Integer, ForeignKey("courses.id"))

    attendance = relationship("Attendance", back_populates="student")
    course = relationship("Course", back_populates="students")
