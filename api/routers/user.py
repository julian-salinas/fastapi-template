#!/usr/bin/env python

import json
from ..database import get_database, get_redis_client
from ..models import User, model_to_dict
from ..schemas import UserCreate
from ..crud import user
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from redis import Redis

router = APIRouter()

# example routes
@router.get("/user", tags = ["users"], response_model = UserCreate)
def get_user(user_id: int, db: Session = Depends(get_database)):
    """ # get_user
    Get a user from the database given its id

    endpoint data
    --------------
    route: /user
    allowed methods: GET, POST

    responses
    ---------
    200: 
        user found
    404: 
        user not found
    500: 
        internal server error
    """
    user_search = user.get_user_by_id(db, user_id)

    if not user_search:
        return JSONResponse(status_code = 404, content = {"message": "User not found!"})

    return user_search


@router.post("/user", tags = ["users"])
async def create_user(user_data: UserCreate = None, db: Session = Depends(get_database), redis_client: Redis = Depends(get_redis_client)):
    """ # create_user
    Create a user with the given data.

    endpoint data
    -----------
    route: /user \n
    allowed methods: GET, POST \n

    responses
    -----------
    201
        User created successfully
    400
        Bad request
    500
        Internal server error
    """
    
    created_user = user.create_user(db, user_data)
    redis_client.set(created_user.username + "#" + str(created_user.id), json.dumps(model_to_dict(created_user)), ex = 1000)
    
    return JSONResponse(status_code = 201, content = model_to_dict(created_user))
