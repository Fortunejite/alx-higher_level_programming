#!/usr/bin/python3
"""Module that returns all the ibject in the database"""


def main(arg):
    """The main function where all the codes are written """
    if len(arg) != 4:
        raise Exception("need 3 arguments!")
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import MetaData
    main(argv)
