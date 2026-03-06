from pydantic import BaseModel,EmailStr

class UserNameCreate(BaseModel):
    name: str
    
class TaskCreate(BaseModel):
    taskname = str
    duration = int
    
    class Config:
        from_attributes=True