#!/usr/bin/python3
import unittest
from models.state import State
from models import storage
import datetime

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
    def test_parent(self):
        self.assertEqual(self.state.name, "")

    def test_state_name(self):
        self.state.name = "Lagos"
        self.state.save()
        key_id = f'{State}.{self.state.id}'
        all_obj = storage.all()
        for key in all_obj.keys():
            if key_id in key:
                self.assertEqual(self.state.name, all_obj[key]['name'])

if __name__ == "__main__":
    unittest.main()