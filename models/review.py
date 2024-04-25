#!/usr/bin/python3
"""this module defines the City for the program"""

from models.base_model import BaseModel


class Review(BaseModel):
    """this class defines the City for the program"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
