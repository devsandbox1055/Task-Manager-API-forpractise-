from sqlalchemy.orm import Session
from app import models
from app import schemas

def create_user(db: Session,user: schemas.UserNameCreate):
    db_user =  models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:Session):
    return db.query(models.User).all()

def get_user(db:Session, User_id:int):
    return db.query(models.User).filter(models.User.username==User_id).first()

def delete_user(db:Session,user_id:int):
    user = get_user(db,user_id)
    if user:
        db.delete(user)
        db.commit()
    return user