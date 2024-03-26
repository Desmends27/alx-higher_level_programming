#!/usr/bin/python3
"""Add a new state to the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
