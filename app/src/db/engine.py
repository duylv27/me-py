"""Create database connection."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.src.db import dbconf

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine.Engine.myengine").setLevel(logging.INFO)

# Create database engine
engine = create_engine(dbconf.SQLALCHEMY_DB_URI, logging_name="myengine")

# Create database session
Session = sessionmaker(bind=engine)
session = Session()