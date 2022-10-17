#!/usr/bin/env python

from api.database import Base
from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

def model_to_dict(model):
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}

# Put your models here

# example
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"User(id = {self.id}, username = {self.username}, age = {self.age})"
