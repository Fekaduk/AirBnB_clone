#!/usr/bin/python3
""" Defines the City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Representing a city.
    Attributes:
        state id (str) : The State id.
        name (str) : The City name.
    """

    state_id = ""
    name = ""
