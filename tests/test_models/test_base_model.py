#!/usr/bin/python3
import unittest, copy
from models.base_model import BaseModel
from datetime import datetime
"""this module defines a unittest class that test for all the edge cases of 
the class BaseModel"""


class Test_for_cases(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.sec_mod_upd = copy.deepcopy(self.my_model)
    def tearDown(self):
        pass
    def test_for_inst(self):
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.created_at, datetime)
    
    def test_is_equal(self):
        self.my_model.num = 89
        self.assertEqual(self.my_model.num, 89)
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)
    
    def test_for_print(self):
        model_str = str(self.my_model)
        expected_str = f"[{self.my_model.__class__.__name__}] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(model_str, expected_str)
    
    def test_for_update(self):
        self.my_model.save()
        self.assertNotEqual(self.sec_mod_upd.updated_at, self.my_model.updated_at)
        self.assertNotEqual(str(self.sec_mod_upd), str(self.my_model))
    
    def test_to_dict(self):
        model = self.my_model.to_dict()
        self.assertIn('updated_at', model)
        self.assertNotEqual(self.sec_mod_upd.updated_at, model['updated_at'])
    
    def test_save(self):
        
    if __name__ == "__main__":
        unittest.main()