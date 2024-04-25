#!/usr/bin/python3
"""unittest for the user class"""

import unittest
from models.user import User
from models import storage
class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.all_objs = storage.all()
    def test_init(self):
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
    
    def test_user_update(self):
        self.user.password = "mojibola0534"
        self.user.email = "lekanmojibola@gmail.com"
        self.user.first_name = "Olalekan"
        self.user.last_name = "Mojibola"

        self.assertEqual(self.user.password, "mojibola0534")
        self.assertEqual(self.user.first_name, "Olalekan")
        self.assertEqual(self.user.last_name, "Mojibola")
        self.assertEqual(self.user.email, "lekanmojibola@gmail.com")
    
    def test_user_save(self):
        self.user.password = "mojibola0534"
        self.user.email = "lekanmojibola@gmail.com"
        self.user.first_name = "Olalekan"
        self.user.last_name = "Mojibola"
        key_user = f"{self.user.__class__.__name__}.{self.user.id}"
        self.user.save()
        for key in self.all_objs.keys():
            if key_user in key:
                self.assertTrue(True)

    
    if __name__ == "__main__":
        unittest.main()
