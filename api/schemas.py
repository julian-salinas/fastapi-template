#!/usr/bin/env python

from pydantic import BaseModel
from typing import List

# Put your schemas here

# example
class UserCreate(BaseModel):
    username: str
    age: int