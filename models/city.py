#!/usr/bin/python
"""
City Class Module
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City Class implementation.

    Attributes:
        __tablename__ (str): MySQL tablename value: cities.
        state_id (str): State identifier.
        name (str): State name.
        places (sqlalchemy.orm.relationship): Places -> Cities relationship.
    
    Methods:
        - __init__: Initializes obj by calling super.
    
    Inherits from:
        BaseModel: Base class for HBNB Clone objects.
        Base: Declarative base for SQLAlchemy table.
    """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
