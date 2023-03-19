#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MeteData

"""Using sqlqlchemy ti create sql tables to python class """


mdata=MetaData()
Base = declarative_base(metadata=mdata)


class State(Base):
    """The model of the state class."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
