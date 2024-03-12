#!/usr/bin/python3
""" Define the BaseModel Class."""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """ Initialized a new BaseModel.
        Args:
            *args (Any): Not used
            **kwargs (dict): Key and Value pairs of attributes
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """ Updates updated_at with the current datetime"""

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Return the dictionary of the BaseModel instance.
        including the key and value pair __class__ representing
        the class name of the object.
        """
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict["updated_at"] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict

    def __str__(self):
        """ Return the string representation of thr BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
