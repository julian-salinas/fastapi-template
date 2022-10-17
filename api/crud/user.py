#!/usr/bin/env python

from sqlalchemy.orm import Session
from ..models import User

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, age: int) -> User:
    user = User(username = username, age = age)

    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user