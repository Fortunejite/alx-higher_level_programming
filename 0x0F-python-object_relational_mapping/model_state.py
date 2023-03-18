#!/usr/bin/python3
"""Using sqlqlchemy ti create sql tables to python class """


def main():
    """The main function for the while operation"""
    Base = declarative_base()
    class State(Base):
        __tablename__ = "states"

        id = Column(Integer(), nullable=False, unique=True, primary_key=True)
        name = Column(String(128), nullable=False, unique=True)

if __name__ == "__main__":
    from SQLAlchemy.orm import declarative_base
    from SQLAlchemy import Column, String, Integer
    main()