#!/usr/bin/python3
"""Module that returns all the ibject in the database"""


def main(arg):
    """The main function where all the codes are written """
    if len(arg) != 5:
        raise Exception("need 4 arguments!")
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == arg[4]).first()
    if states:
        print(f"{states.id}")
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import MetaData
    main(argv)
