#!/usr/bin/pyhon3
"""Module that returns all the ibject in the database"""


def main(arg):
    """The main function where all the codes are written """
    if len(arg) != 4:
        raise Exception("need 3 arguments!")
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(states.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    main(argv)
