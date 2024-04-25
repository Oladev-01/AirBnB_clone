#!/usr/bin/python3
"""this module creates a new user and assign a new id to them and
then save to storage"""

from models.base_model import BaseModel


class User(BaseModel):
    """this class creates a new user"""
    [email, first_name, last_name, password] = ["", "", "", ""]

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, *kwargs)
