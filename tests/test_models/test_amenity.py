#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models import storage
import datetime

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
    def test_parent(self):
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name(self):
        self.amenity.name = "Bedroom"
        self.assertEqual(self.amenity.name, "Bedroom")

if __name__ == "__main__":
    unittest.main()