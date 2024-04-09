#!/usr/bin/python3
import uuid
from datetime import datetime
"""This module contains the base class for all classes that would be
written and used for the project"""


class BaseModel:
    """This is the base class for all classes that will be used
      in this project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """this method updates the datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """this method updates the format of the datetime
          and also add the base class name to
        dict of its instances"""
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
