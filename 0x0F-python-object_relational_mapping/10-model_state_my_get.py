#!/usr/bin/python3
""" Prints the state object witht he name passed as argument """

from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    select = session.query(State).filter(State.name.like(argv[4]))

    result = select.first()

    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()
