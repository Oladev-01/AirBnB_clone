#!/usr/bin/python3
"""this module creates a new user and assign a new id to them and
then save to storage"""

from models.base_model import BaseModel


class User(BaseModel):
    """this class creates a new user"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, *kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
