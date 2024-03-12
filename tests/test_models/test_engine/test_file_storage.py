#!/usr/bin/python3
""" Defines unittests for models/engine/file_storage.py
unittests class:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.state import State


class TestFileStorage_instantiation(unittest.TestCase):
    """ Unittests for instantiation of the FileStorage class """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))



class TestFileStorage_methods(unittest.TestCase):
    """ Unittests for methods of the FileStorage class """

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
        FileStorage._FileStorage__objects = {}


    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bmodel = BaseModel()
        usr = User()
        ste = State()
        plc = Place()
        cty = City()
        amy = Amenity()
        rvw = Review()
        models.storage.new(bmodel)
        models.storage.new(usr)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amy)
        models.storage.new(rvw)
        self.assertIn("BaseModel." + bmodel.id, models.storage.all().keys())
        self.assertIn(bmodel, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + ste.id, models.storage.all().keys())
        self.assertIn(ste, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amy.id, models.storage.all().keys())
        self.assertIn(amy, models.storage.all().values())
        self.assertIn("Review." + rvw.id, models.storage.all().keys())
        self.assertIn(rvw, models.storage.all().values())


    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bmodel = BaseModel()
        usr = User()
        ste = State()
        plc = Place()
        cty = City()
        amy = Amenity()
        rvw = Review()
        models.storage.new(bmodel)
        models.storage.new(usr)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amy)
        models.storage.new(rvw)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
        self.assertIn("BaseModel." + bmodel.id, save_text)
        self.assertIn("User." + usr.id, save_text)
        self.assertIn("State." + ste.id, save_text)
        self.assertIn("Place." + plc.id, save_text)
        self.assertIn("City." + cty.id, save_text)
        self.assertIn("Amenity." + amy.id, save_text)
        self.assertIn("Review." + rvw.id, save_text)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bmodel = BaseModel()
        usr = User()
        ste = State()
        plc = Place()
        cty = City()
        amy = Amenity()
        rvw = Review()
        models.storage.new(bmodel)
        models.storage.new(usr)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amy)
        models.storage.new(rvw)
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bmodel.id, objs)
        self.assertIn("User." + usr.id, objs)
        self.assertIn("State." + ste.id, objs)
        self.assertIn("Place." + plc.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + amy.id, objs)
        self.assertIn("Review." + rvw.id, objs)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
