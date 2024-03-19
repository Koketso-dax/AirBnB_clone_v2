#!/usr/bin/python3
""" Holds Place class module """
from os import getenv
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    """Representation of Place """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete", backref="places")
        amenities = relationship("Amenity", secondary='place_amenity', viewonly=False, backref="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute that returns list of Review instances"""
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            return [review for review in self.reviews if review.place_id == self.id]
        else:
            return [review for review in models.storage.all("Review").values() if review.place_id == self.id]

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                return [amenity for amenity in self.amenities if amenity.place_id == self.id]
            else:
                return [amenity for amenity in models.storage.all("Amenity").values() if amenity.place_id == self.id]
