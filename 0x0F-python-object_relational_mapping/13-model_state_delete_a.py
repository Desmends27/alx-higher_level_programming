#!/usr/bin/python3
"""Delete a state object from the database """

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
