#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amy = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amy.__dict__)

    def test_two_amenities_unique_ids(self):
        amy1 = Amenity()
        amy2 = Amenity()
        self.assertNotEqual(amy1.id, amy2.id)

    def test_two_amenities_different_created_at(self):
        amy1 = Amenity()
        sleep(0.05)
        amy2 = Amenity()
        self.assertLess(amy1.created_at, amy2.created_at)

    def test_two_amenities_different_updated_at(self):
        amy1 = Amenity()
        sleep(0.05)
        amy2 = Amenity()
        self.assertLess(amy1.updated_at, amy2.updated_at)

    def test_str_representation(self):
        dtime = datetime.today()
        dtime_repr = repr(dtime)
        amy = Amenity()
        amy.id = "123456789"
        amy.created_at = amy.updated_at = dtime
        amystr = amy.__str__()
        self.assertIn("[Amenity] (123456789)", amystr)
        self.assertIn("'id': '123456789'", amystr)
        self.assertIn("'created_at': " + dtime_repr, amystr)
        self.assertIn("'updated_at': " + dtime_repr, amystr)

    def test_args_unused(self):
        amy = Amenity(None)
        self.assertNotIn(None, amy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dtime = datetime.today()
        dtime_iso = dtime.isoformat()
        amy = Amenity(id="345", created_at=dtime_iso, updated_at=dtime_iso)
        self.assertEqual(amy.id, "345")
        self.assertEqual(amy.created_at, dtime)
        self.assertEqual(amy.updated_at, dtime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        amy = Amenity()
        sleep(0.05)
        first_updated_at = amy.updated_at
        amy.save()
        self.assertLess(first_updated_at, amy.updated_at)

    def test_two_saves(self):
        amy = Amenity()
        sleep(0.05)
        first_updated_at = amy.updated_at
        amy.save()
        second_updated_at = amy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amy.save()
        self.assertLess(second_updated_at, amy.updated_at)

    def test_save_with_arg(self):
        amy = Amenity()
        with self.assertRaises(TypeError):
            amy.save(None)

    def test_save_updates_file(self):
        amy = Amenity()
        amy.save()
        amyid = "Amenity." + amy.id
        with open("file.json", "r") as f:
            self.assertIn(amyid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amy = Amenity()
        self.assertIn("id", amy.to_dict())
        self.assertIn("created_at", amy.to_dict())
        self.assertIn("updated_at", amy.to_dict())
        self.assertIn("__class__", amy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amy = Amenity()
        amy.middle_name = "School"
        amy.my_number = 98
        self.assertEqual("School", amy.middle_name)
        self.assertIn("my_number", amy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amy = Amenity()
        amy_dict = amy.to_dict()
        self.assertEqual(str, type(amy_dict["id"]))
        self.assertEqual(str, type(amy_dict["created_at"]))
        self.assertEqual(str, type(amy_dict["updated_at"]))

    def test_to_dict_output(self):
        dtime = datetime.today()
        amy = Amenity()
        amy.id = "123456"
        amy.created_at = amy.updated_at = dtime
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dtime.isoformat(),
            'updated_at': dtime.isoformat(),
        }
        self.assertDictEqual(amy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amy = Amenity()
        self.assertNotEqual(amy.to_dict(), amy.__dict__)

    def test_to_dict_with_arg(self):
        amy = Amenity()
        with self.assertRaises(TypeError):
            amy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
