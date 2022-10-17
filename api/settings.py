#!/usr/bin/env python

import os
from fastapi.logger import logger
import logging
from logging.handlers import RotatingFileHandler
from pydantic import BaseSettings, Field

def log_create(logfile: str = "logfile.log"):
    log = logging.getLogger("fastapi")

    formatter = logging.Formatter(
        "[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")

    handler = RotatingFileHandler(logfile, backupCount=0)

    logger.addHandler(handler)

    handler.setFormatter(formatter)

    return log

class Settings(BaseSettings):
    # Application
    host: str = Field("0.0.0.0", env = "HOST")
    port: int = Field(8000, env = "PORT")
    
    # Database (postgres)
    db_url: str = Field(f'postgresql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@database:5432/database_name', env="DATABASE_URL")

    # Redis
    redis_host: str = Field("cache", env = "REDIS_HOST")
    redis_port: int = Field(6379, env = "REDIS_PORT")
    redis_password: str = Field(os.getenv("REDIS_PASSWORD"), env = "REDIS_PASSWORD")


settings = Settings()