#!/usr/bin/python3
import unittest
from models.place import Place
from models import storage
import datetime

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_parent(self):
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_state_instances(self):
        self.place.name = "uniosun"
        self.place.city_id = "1234"
        self.place.user_id = "1-2"
        self.place.description = "An institution"

        self.assertEqual(self.place.name, "uniosun")
        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "1-2")
        self.assertEqual(self.place.description, "An institution")

if __name__ == "__main__":
    unittest.main()