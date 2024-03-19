#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
