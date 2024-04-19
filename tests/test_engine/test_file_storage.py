#!/usr/bin/python3
import unittest
from models import storage
from models.engine.file_storage import FileStorage
import json, os
from models.base_model import BaseModel

class Test_for_storage(unittest.TestCase):
    def setUp(self):
        self.all_objs = storage.all()
        self.test_data = {"TestModel.1234": {"id": "1234", "name": "Test"}}
        with open("test_file.json", "w") as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        os.remove("test_file.json")
    def test_file_path(self):
        file_path = FileStorage.get_file_path()
        self.assertEqual(file_path, "file.json")

    def test_reload(self):
        store = FileStorage()
        store._FileStorage__file_path = "test_file.json"
        store.reload()
        self.assertEqual(store.all(), self.test_data)

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
    
    if __name__ == "__main__":
        unittest.main()