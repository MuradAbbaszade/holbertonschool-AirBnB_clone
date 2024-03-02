#!/usr/bin/python3
"""
Unittest for User Class attributes and methods
"""
from unittest import TestCase
from datetime import datetime
from models.user import User


class TestUser(TestCase):
    """Defines variables and methods"""
    def setUp(self):
        """
        Sets up the public attributes and methods for the TestUser class
        """
        self.inst = User()
        self.inst.created_at = datetime.now()
        self.inst.updated_at = datetime.now()
        self.user = User()

    def test_id(self):
        self.model_test = User()
        self.assertNotEqual(self.inst.id, self.model_test.id)

    def test_save(self):
        updated_at = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(updated_at, self.inst.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("User.{}".format(self.inst.id), file.read())

    def test_to_dict(self):
        new = self.inst.to_dict()
        self.assertEqual(new["created_at"], self.inst.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.inst.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.inst.__class__.__name__)







"""    from models.base_model import BaseModel

    class User(BaseModel):
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        """