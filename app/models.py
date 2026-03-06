from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "tasks"

    username = Column(String, primary_key=True, nullable=False)
    tasksname = Column(String, nullable=False)
    duration = Column(Integer, unique=True, nullable= False)