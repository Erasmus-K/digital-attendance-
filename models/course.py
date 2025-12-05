from sqlalchemy import Column, Integer, String
from config.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
