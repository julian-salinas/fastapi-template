#!/usr/bin/env python

import os
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, Response, HTTPException

from .settings import log_create
from .database import engine, get_database
from .models import Base
from .schemas import *
from .routers.user import router as user_router

Base.metadata.create_all(bind=engine)

log = log_create(logfile = "general.log")

app = FastAPI()
app.include_router(user_router)

@app.get("/", tags = ["general"])
def index():
    log.info("Request received!")
    return JSONResponse(status_code = 200, content = {"message": "Hello from FastAPI!"})
