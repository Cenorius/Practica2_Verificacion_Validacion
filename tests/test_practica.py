# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
import pymongo
import mongomock
import mock
from practica.data_base import data_base


class data_base_TestDB(TestCase):
    def setUp(self):
        self.data_base = data_base()
        self.data_base.db = mongomock.MongoClient()[self.data_base.DATA_BASE_NAME]

    def tearDown(self):
        self.data_base.db.drop_collection('words')

# -test_insert---------------------------------------------------------------------------------------------

    def test_insert_element_existing_in_db(self):
        element = {"name":"texto",'words': [{'palabra1': 1}, {'palabra2': 2}]}

        self.data_base._exist=mock.MagicMock(return_value=True)

        self.assertIsNone(self.data_base.insert(element))

    def test_insert_element_not_existing_in_db(self):
        element = {"name":"texto",'words': [{'palabra1': 1}, {'palabra2': 2}]}
        
        self.data_base._exist=mock.MagicMock(return_value=True)

        self.assertIsNone(self.data_base.insert(element))

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
    def test_delete_one_element_not_existing_in_db(self):
        result=self.data_base.delete("1").deleted_count
        expected=0

        self.assertEqual(result,expected)

    def test_delete_one_element_existing_in_db(self):
        id=self.data_base.insert({"name":"texto",'words': [{'palabra1': 1}, {'palabra2': 2}]})
        
        result=self.data_base.delete(id).deleted_count
        expected=1

        self.assertEqual(result,expected)

        

# -test_update------------------------------------------------------------------------------------------------
    def test_update_one_existing_in_db(self):
        element={"name":"texto",'words': [{'palabra1': 1}, {'palabra2': 2}]}
        id=self.data_base.insert(element)

        result=self.data_base.update(element,id).matched_count
        expected=1

        self.assertEquals(result,expected)
    
    def test_update_one_not_existing_in_db(self):
        element={"name":"texto",'words': [{'palabra1': 1}, {'palabra2': 2}]}
        id="id"

        result=self.data_base.update(element,id).matched_count
        expected=0

        self.assertEquals(result,expected)

    def test_update_one_integer(self):
        element = 1
        id="id"

        with self.assertRaises(TypeError):
            self.data_base.update(element,id)

    def test_update_one_list(self):
        element = []
        id="id"

        with self.assertRaises(TypeError):
            self.data_base.update(element,id)

    def test_update_one_str(self):
        element = 'test'
        id="id"

        with self.assertRaises(TypeError):
            self.data_base.update(element,id)

    def test_update_one_unicode(self):
        element = u'test'
        id="id"

        with self.assertRaises(TypeError):
            self.data_base.update(element,id)

# -test__exist------------------------------------------------------------------------------------------------

    def test_exist_not_existing_element_in_db(self):
        element = {"name":"texto",'words': [{'palabra1': 2}, {'palabra2': 2}]}

        self.assertFalse(self.data_base._exist(element))

    def test_alive(self):
        self.assertTrue(self.data_base._alive())
