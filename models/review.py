#!/usr/bin/python3
""" Defines a Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """ Representing a review.
    Attributes:
        place_id (str) : The Place id.
        user_id (str) : The User id.
        text (str) : The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
