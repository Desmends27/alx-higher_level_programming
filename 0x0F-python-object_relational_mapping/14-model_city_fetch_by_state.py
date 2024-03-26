#!/usr/bin/python3
"""Prints all the city objects from the database """

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)

    result = session.query(City, State).\
        join(City, City.state_id == State.id)\
        .order_by(City.id).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
