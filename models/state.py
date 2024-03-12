#!/usr/bin/python3
""" Defines the State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Representing a State.
    Attributes:
        name (str) : Name of State.
    """

    name = ""
