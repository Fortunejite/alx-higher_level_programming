#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey
"""Using sqlqlchemy ti create sql tables to python class """


class City(Base):
    """The model of the state class."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
