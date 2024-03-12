#!/usr/bin/python3
""" Defines unittests for models/base_models.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel_instantiation(unittest.TestCase):
    """ Unittest for testing instantiation of BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bmodel1 = BaseModel()
        bmodel2 = BaseModel()
        self.assertNotEqual(bmodel1.id, bmodel2.id)

    def test_two_models_different_created_at(self):
        bmodel1 = BaseModel()
        sleep(0.10)
        bmodel2 = BaseModel()
        self.assertLess(bmodel1.created_at, bmodel2.created_at)

    def test_two_models_different_updated_at(self):
        bmodel1 = BaseModel()
        sleep(0.10)
        bmodel2 = BaseModel()
        self.assertLess(bmodel1.updated_at, bmodel2.updated_at)

    def test_str_representation(self):
        dtime = datetime.today()
        dtime_repr = repr(dtime)
        bmodel = BaseModel()
        bmodel.id = "123456789"
        bmodel.created_at = bmodel.updated_at = dtime
        bmodelstr = bmodel.__str__()
        self.assertIn("[BaseModel] (123456789)", bmodelstr)
        self.assertIn("'id': '123456789'", bmodelstr)
        self.assertIn("'created_at': " + dtime_repr, bmodelstr)
        self.assertIn("'updated_at': " + dtime_repr, bmodelstr)

    def test_args_not_used(self):
        bmodel = BaseModel(None)
        self.assertNotIn(None, bmodel.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dtime = datetime.today()
        dtime_iso = dtime.isoformat()
        bmodel = BaseModel(id = "345", created_at = dtime_iso, updated_at = dtime_iso)
        self.assertEqual(bmodel.id, "345")
        self.assertEqual(bmodel.created_at, dtime)
        self.assertEqual(bmodel.updated_at, dtime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id = None, created_at = None, updated_at = None)

    def test_instantiation_with_args_and_kwargs(self):
        dtime = datetime.today()
        dtime_iso = dtime.isoformat()
        bmodel = BaseModel("12", id = "345", created_at = dtime_iso, updated_at = dtime_iso)
        self.assertEqual(bmodel.id, "345")
        self.assertEqual(bmodel.created_at, dtime)
        self.assertEqual(bmodel.updated_at, dtime)


class TestBaseModel_save(unittest.TestCase):
    """ Unittest for save method of the BaseModel Class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass


    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


    def test_one_save(self):
        bmodel = BaseModel()
        sleep(0.05)
        first_updated_at = bmodel.updated_at
        bmodel.save()
        self.assertLess(first_updated_at, bmodel.updated_at)

    def test_two_saves(self):
        bmodel = BaseModel()
        sleep(0.05)
        first_updated_at = bmodel.updated_at
        bmodel.save()
        second_updated_at = bmodel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bmodel.save()
        self.assertLess(second_updated_at, bmodel.updated_at)

    def test_save_with_args(self):
        bmodel = BaseModel()
        with self.assertRaises(TypeError):
            bmodel.save(None)

    def test_save_updates_file(self):
        bmodel = BaseModel()
        bmodel.save()
        bmodelid = "BaseModel." + bmodel.id
        with open("file.json", "r") as f:
            self.assertIn(bmodelid, f.read())



class TestBaseModel_to_dict(unittest.TestCase):
    """ Unittests for _to_dict methond of the BaseModel class"""

    def test_to_dict_type(self):
        bmodel = BaseModel()
        self.assertTrue(dict, type(bmodel.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bmodel = BaseModel()
        self.assertIn("id", bmodel.to_dict())
        self.assertIn("created_at", bmodel.to_dict())
        self.assertIn("updated_at", bmodel.to_dict())
        self.assertIn("__class__", bmodel.to_dict())

    def test_to_dict_contains_added_attribites(self):
        bmodel = BaseModel()
        bmodel.name = "School"
        bmodel.my_number = 98
        self.assertIn("name", bmodel.to_dict())
        self.assertIn("my_number", bmodel.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bmodel = BaseModel()
        bmodel_dict = bmodel.to_dict()
        self.assertEqual(str, type(bmodel_dict["created_at"]))
        self.assertEqual(str, type(bmodel_dict["updated_at"]))

    def test_to_dict_output(self):
        dtime = datetime.today()
        bmodel = BaseModel()
        bmodel.id = "123456789"
        bmodel.created_at = bmodel.updated_at = dtime
        tdict = {
            'id' : '123456789',
            '__class__' : 'BaseModel',
            'created_at' : dtime.isoformat(),
            'updated_at' : dtime.isoformat()
        }
        self.assertDictEqual(bmodel.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bmodel = BaseModel()
        self.assertNotEqual(bmodel.to_dict(), bmodel.__dict__)

    def test_to_dict_with_args(self):
        bmodel = BaseModel()
        with self.assertRaises(TypeError):
            bmodel.to_dict(None)




if __name__ == "__main__":
    unittest.main()
