#!/usr/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

"""Using sqlqlchemy ti create sql tables to python class """


Base = declarative_base()
class State(Base):
    __tablename__ = "states"

    id = Column(Integer(), nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
