#!/usr/bin/python3
"""User class module"""
from os import getenv
from hashlib import md5
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Representation of a user """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Getter property for password"""
        return self._password

    @password.setter
    def password(self, pwd):
        """Setter property for password"""
        self._password = md5(pwd.encode()).hexdigest()
