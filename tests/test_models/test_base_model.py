import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        self.base_model = BaseModel()
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(old_updated_at, base_model.updated_at)

    def test_save_method_with_storage(self):
        base_model = BaseModel()
        base_model.name = "Model"
        base_model.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIn("BaseModel." + base_model.id, storage.all())

    def test_to_dict(self):
        self.base_model = BaseModel()
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        
    def test_str_method(self):
        base_model = BaseModel()
        exp_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), exp_str)

        if __name__ == '__main__':
            unittest.main()
