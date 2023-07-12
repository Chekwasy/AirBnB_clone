# test_BaseModel_class.py

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ unittest for testing class BaseModel """

    def setUp(self):
        self.model = BaseModel()

    def test_attributes(self):
        """ check if the BaseModel instance has the correct attributes """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.name, None)
        self.assertEqual(self.model.my_number, 0)

    def test_str_representation(self):
        """ Test the string representation of the BaseModel instance """
        expected = "[BaseModel](" + self.model.id + ")" \
            + str(self.model.__dict__)
        self.assertEqual(str(self.model), expected)

    def test_to_dict(self):
        """ Test the to_dict method of the BaseModel instance """
        expected = {
            "my_number": self.model.my_number,
            "name": self.model.name,
            "updated_at": self.model.updated_at.isoformat(),
            "id": self.model.id,
            "created_at": self.model.created_at.isoformat()
        }
        self.assertDictEqual(self.model.to_dict(), expected)

    def test_save(self):
        """ Test the save method of the BaseModel instance """
        old_update = self.model.updated_at
        self.model.save()
        new_update = self.model.updated_at
        self.assertGreater(new_update, old_update)


if __name__ == '__main__':
    unittest.main()
