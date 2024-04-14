#!/usr/bin/python3
import json
"""this module defines the storage engine for the class"""


class FileStorage:
    """this class saves and writes each instances of the class
    created to a json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this method returns the __objects which is a dictionary
          containing all instances of the class BaseModel"""
        return FileStorage.__objects

    def new(self, obj):
        """this method adds a new instance to the dictionary with a key syntax
        of BaseModel.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    @classmethod
    def get_file_path(cls):
        return cls.__file_path
    def save(self):
        """this method saves the dictionary instances of the class created and
        writes them to the json file"""
        store = FileStorage.__objects
        serial = {key: inst.to_dict() for key, inst in store.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serial, f)

    def reload(self):
        """this method reloads all instances that have been saved in the
        json file deserializing them"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                de_serial = json.load(f)
                for key, value in de_serial.items():
                    cls_name, ob_id = key.split('.')
                    module = __import__("models.base_model",
                                        fromlist=[cls_name])
                    cls = getattr(module, cls_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
