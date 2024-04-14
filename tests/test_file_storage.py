#!/usr/bin/python3
import unittest
from models import storage
import json
from models.base_model import BaseModel

class Test_for_storage(unittest.TestCase):
    def setUp(self):
        self.all_objs = storage.all()
    
    def test_reload(self):
        for key in self.all_objs.keys():
            obj = self.all_objs[key]
            print(obj)

    def test_inst(self):
        self.model = BaseModel()
        self.model.name = "First Model"
        self.model.num = 34
        self.model.save()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertTrue(key in self.all_objs.keys())    
    def test_json(self):
        try:
            with open("file.json", 'r') as f:
                file = json.load(f)
            self.assertTrue(isinstance(file, dict))
        except FileNotFoundError:
            pass