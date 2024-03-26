#!/usr/bin/python3
"""Update a state in the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).where(State.id == 2).first()
    print(state.name)
    state.name = 'New Mexico'
    session.commit()
    session.close()
