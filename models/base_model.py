#!/usr/bin/python3
import uuid
from datetime import datetime
"""This is the base class for all classes that would be
written and used for the project"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{0}] ({1}) {2}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
