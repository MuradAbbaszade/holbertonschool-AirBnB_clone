import unittest
from datetime import datetime
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        self.base_model = BaseModel()
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.base_model.updated_at.isoformat())

        if __name__ == '__main__':
            unittest.main()
