#!/usr/bin/python3
"""
Unittest for Amenity Class attributes and methods
"""
from unittest import TestCase
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(TestCase):
    """Defines variables and methods"""
    def setUp(self):
        """
        Sets up the public attributes and methods for the TestUser class
        """
        self.inst1 = Amenity()
        self.inst1.created_at = datetime.now()
        self.inst1.updated_at = datetime.now()
        self.inst2 = Amenity()

    def test_id(self):
        self.model_test = Amenity()
        self.assertNotEqual(self.inst1.id, self.model_test.id)

    def test_save(self):
        updated_at = self.inst1.updated_at
        self.inst1.save()
        self.assertNotEqual(updated_at, self.inst1.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Amenity.{}".format(self.inst1.id), file.read())

    def test_to_dict(self):
        new = self.inst1.to_dict()
        self.assertEqual(new["created_at"], self.inst1.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.inst1.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.inst1.__class__.__name__)

    def test__str__(self):
        className = self.inst1.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.inst1.id, self.inst1.__dict__)
        self.assertEqual(result, self.inst1.__str__())

    def test_name(self):
        self.assertTrue(hasattr(self.inst2, "name"))
        self.assertEqual(self.inst2.name, "")