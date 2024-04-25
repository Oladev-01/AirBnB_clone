#!/usr/bin/python3
"""This module contains the base class for all classes that would be
written and used for the project"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the base class for all classes that will be used
      in this project"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """this method updates the datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """this method updates the format of the datetime
          and also add the base class name to
        dict of its instances"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = \
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict['updated_at'] = \
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
