#!/usr/bin/python3
"""Contains the City class definition"""
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """City tabale creation"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
