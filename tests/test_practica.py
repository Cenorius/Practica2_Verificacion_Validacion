from unittest import TestCase
import unittest
import mongomock
import mock
from practica.data_base import data_base


# enconding: utf-8

class data_base_TestDB(TestCase):
    def setUp(self):
        self.data_base = data_base()
        self.data_base.db = mongomock.MongoClient()[self.data_base.DATA_BASE_NAME]

    def tearDown(self):
        self.data_base.db.drop_collection('words')

    # -test_insert---------------------------------------------------------------------------------------------

    def test_insert_element_existing_in_db(self):
        element = {'texto': [{'palabra1': 1}, {'palabra2': 2}]}

        self.data_base._exist=mock.MagicMock(return_value=True)

        self.assertFalse(self.data_base.insert(element))

    def test_insert(self):
        element = {'texto2': [{'palabra1': 1}, {'palabra2': 2}]}

        self.assertFalse(self.data_base.insert(element))

    def test_insert_integer(self):
        element = 1

        with self.assertRaises(TypeError):
            self.data_base.insert(element)

    def test_insert_list(self):
        element = []

        with self.assertRaises(TypeError):
            self.data_base.insert(element)

    def test_insert_str(self):
        element = 'test'

        with self.assertRaises(TypeError):
            self.data_base.insert(element)

    def test_insert_unicode(self):
        element = u'test'

        with self.assertRaises(TypeError):
            self.data_base.insert(element)

            # -test_delete------------------------------------------------------------------------------------------------
    def test__delete_one(self):
        self.data_base.delete({'_id': 1})
        self.assertTrue(self.data_base._exist({'id':1}))


            # -test_update------------------------------------------------------------------------------------------------



            # -test__exist------------------------------------------------------------------------------------------------

    def test__exist_not_existing_element_in_db(self):
        element = {'texto3': [{'palabra1': 2}, {'palabra2': 2}]}

        self.assertFalse(self.data_base._exist(element))

    def test__alive(self):
        self.assertTrue(self.data_base._alive())
