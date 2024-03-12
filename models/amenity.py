#!/usr/bin/python3
""" Defines the Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Representing an amenity.
    Attributes:
        name (str) : Amenity name
    """

    name = ""
