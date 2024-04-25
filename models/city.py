#!/usr/bin/python3
"""this module defines the City for the program"""

from models.base_model import BaseModel


class City(BaseModel):
    """this class defines the City for the program"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
