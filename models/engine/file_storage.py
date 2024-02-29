#!/usr/bin/python3
"""File storage module."""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All function"""
        return FileStorage.__objects

    def new(self, obj):
        """New function"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save function"""
        new_objects = {}
        for key, value in FileStorage.__objects.items():
            new_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_objects, file)

    def reload(self):
        """Reload function"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_obj = json.load(file)
            for key in json_obj:
                FileStorage.__objects[key] = BaseModel(**json_obj[key])
        except Exception:
            pass
