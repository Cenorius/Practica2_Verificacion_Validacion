from unittest import TestCase
from practica.data_base import data_base

import mock
import mongomock

class data_base_TestDB(TestCase):

    def setUp(self):
        self.data_base=data_base()
        self.data_base.db=mongomock.MongoClient()[self.db.DATA_BASE_NAME]

    def tearDown(self):
        self.data_base.db.drop_collection('words')

#-test_insert---------------------------------------------------------------------------------------------

    def test_insert_element_existing_in_db(self):
        element={'texto':[{'palabra1':1},{'palabra2':2}]}
        
        self.data_base.insert(element)

        self.assertFalse(self.data_base.insert(element))

    def test_insert(self):
        element={'texto2':[{'palabra1':1},{'palabra2':2}]}

        self.assertTrue(self.data_base.insert(element))
    
    def test_insert_integer(self):
        element=1

        with self.assertRaises(TypeError):
			self.data_base.insert(element)

    def test_insert_list(self):
        element=[]

        with self.assertRaises(TypeError):
			self.data_base.insert(element)

    def test_insert_str(self):
        element='test'

        with self.assertRaises(TypeError):
			self.data_base.insert(element)

    def test_insert_unicode(self):
        element=u'test'

        with self.assertRaises(TypeError):
			self.data_base.insert(element)    

#-test_delete------------------------------------------------------------------------------------------------


#-test_update------------------------------------------------------------------------------------------------



#-test__exist------------------------------------------------------------------------------------------------

    def test__exist_not_existing_element_in_db(self):
        element={'texto3':[{'palabra1':1},{'palabra2':2}]}

        self.assertFalse(self.data_base._exist(element))