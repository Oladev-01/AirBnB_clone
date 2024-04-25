#!/usr/bin/python3
"""this module defines a class that defines the State inheriting
from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """this module defines the states for the program"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
