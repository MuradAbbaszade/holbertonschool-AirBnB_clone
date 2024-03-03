#!/usr/bin/python3
"""
Unittest for To check FileStorage Class attributes and methods
"""
from unittest import TestCase
from models.base_model import BaseModel
import os
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """Defines variables and methods"""
    def setUp(self):
        """
        Sets up the public attributes and methods for the TestUser class
        """
        self.f1 = FileStorage()
        self.inst1 = BaseModel()
        self.file_path = "file.json"
        self.object = {"BaseModel.123": {"id": "123", "name": "test"}}

        with open(self.file_path, "w") as f:
            json.dump(self.object, f)

    def test_atributes(self):
        self.assertIsInstance(self.f1._FileStorage__file_path, str)
        self.assertIsInstance(self.f1._FileStorage__objects, dict)

    def test_new(self):
        self.assertIn(self.inst1, self.f1.all().values())

    def test_save(self):
        self.f1.new(self.inst1)
        self.f1.save()

        with open(self.file_path, "r") as f:
            read_data = f.read()
            name = self.inst1.__class__.__name__
        self.assertIn("{}.{}".format(name, self.inst1.id), read_data)

    def test_reload(self):
        self.f1.save()
        self.f1._FileStorage__objects.clear()
        self.f1.reload()
        self.assertNotEqual(len(self.f1._FileStorage__objects), 0)

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except IOError:
            pass