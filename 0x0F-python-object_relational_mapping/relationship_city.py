#!/usr/bin/python3
""" Module contains class definition for the model_city
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State

Base = declarative_base()


class City(Base):
    """ City class definition
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
