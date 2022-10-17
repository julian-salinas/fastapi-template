#!/usr/bin/env python

import os
from redis import Redis
from api.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.db_url)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

def get_database(): 
    """
    @DEPENDENCY \n
    @NAME: get_database \n
    @DESC: Crea y retorna una sesión para acceder a la base de datos \n
    """

    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()
    
def get_redis_client():
    """
    @DEPENDENCY \n
    @NAME: get_redis_client \n
    @DESC: Crea y retorna un cliente para acceder a la base de datos redis \n
    """

    redis_client = Redis(host = settings.redis_host, port = settings.redis_port, password = settings.redis_password)

    try:
        yield redis_client
    
    finally:
        redis_client.close()