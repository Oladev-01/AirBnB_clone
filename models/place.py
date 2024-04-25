#!/usr/bin/python3
"""this module defines the City for the program"""

from models.base_model import BaseModel


class Place(BaseModel):
    """this class defines the City for the program"""
    [name, city_id, user_id, description, number_rooms,
     number_bathrooms, max_guest, price_by_night,
     latitude, longitude, amenity_ids] = \
        ["", "", "", "", 0, 0, 0, 0, 0.0, 0.0, []]

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
