#!/usr/bin/python3
import unittest
from models.city import City
from models import storage
import datetime

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
    def test_parent(self):
        self.assertEqual(self.city.name, "")

    def test_state_name(self):
        self.city.name = "Ikeja"
        self.assertEqual(self.city.name, "Ikeja")

if __name__ == "__main__":
    unittest.main()