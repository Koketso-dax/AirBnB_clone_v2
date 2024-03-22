#!/usr/bin/python
""" Amenity class module """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity Class implementation.

    Attributes:

        __tablename__ (str): SQL tablename value: amenities.
        name (str): Amenity field name.

    Methods:
        - __init__: initializes obj by calling super constructor.

    Inherits from:
        BaseModel: Super class for all data in HBNB Clone.
        Base: Declarative base for SQLAlchemy.
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity instance.

        Args:

        *args (list): argument list.
        **kwargs (dict): keyword args.
        """
        super().__init__(*args, **kwargs)
