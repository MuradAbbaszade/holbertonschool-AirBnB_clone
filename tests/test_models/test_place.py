#!/usr/bin/python3
"""
Unittest for Place Class attributes and methods
"""
from unittest import TestCase
from datetime import datetime
from models.place import Place


class TestUser(TestCase):
    """Defines variables and methods"""
    def setUp(self):
        """
        Sets up the public attributes and methods for the TestUser class
        """
        self.inst = Place()
        self.inst.created_at = datetime.now()
        self.inst.updated_at = datetime.now()
        self.user = Place()

    def test_id(self):
        """Tests the UUID for that instance"""
        self.model_test = Place()
        self.assertNotEqual(self.inst.id, self.model_test.id)

    def test_save(self):
        updated_at = self.inst.updated_at
        self.inst.save()
        self.assertNotEqual(updated_at, self.inst.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Place.{}".format(self.inst.id), file.read())

    def test_to_dict(self):
        new = self.inst.to_dict()
        self.assertEqual(new["created_at"], self.inst.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.inst.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.inst.__class__.__name__)

    def test__str__(self):
        className = self.inst.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.inst.id, self.inst.__dict__)
        self.assertEqual(result, self.inst.__str__())

    def test_city_id(self):
        self.assertTrue(hasattr(self.inst, "city_id"))
        self.assertEqual(self.inst.city_id, "")

    def test_user_id(self):
        self.assertTrue(hasattr(self.inst, "user_id"))
        self.assertEqual(self.inst.user_id, "")

    def test_name(self):
        self.assertTrue(hasattr(self.inst, "name"))
        self.assertEqual(self.inst.name, "")

    def test_description(self):
        self.assertTrue(hasattr(self.inst, "description"))
        self.assertEqual(self.inst.description, "")

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.inst, "number_rooms"))
        self.assertEqual(self.inst.number_rooms, 0)

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.inst, "number_bathrooms"))
        self.assertEqual(self.inst.number_bathrooms, 0)

    def test_max_guest(self):
        self.assertTrue(hasattr(self.inst, "max_guest"))
        self.assertEqual(self.inst.max_guest, 0)

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.inst, "price_by_night"))
        self.assertEqual(self.inst.price_by_night, 0)

    def test_latitude(self):
        self.assertTrue(hasattr(self.inst, "latitude"))
        self.assertEqual(self.inst.latitude, 0.0)

    def test_longitude(self):
        self.assertTrue(hasattr(self.inst, "longitude"))
        self.assertEqual(self.inst.longitude, 0.0)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.inst, "amenity_ids"))
        self.assertEqual(self.inst.amenity_ids, [])