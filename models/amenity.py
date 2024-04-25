#!/usr/bin/python3
"""this module defines the City for the program"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """this class defines the City for the program"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
