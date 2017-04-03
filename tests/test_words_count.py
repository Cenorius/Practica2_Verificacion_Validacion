# -*- coding: utf-8 -*-
from .context import practica
import unicodedata


import unittest

class words_count_TestSuite(unittest.TestCase):

#---Test_count----------------------------------------------------------------------------------------------
	
	def test_count_unicode(self):
		
		str=u"bicicleta bicicleta hola bien bien bien"
		
		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_string(self):
		
		str="bicicleta bicicleta hola bien bien bien"
		
		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_acents_string(self):

		str='bicicleta bicicletá hola bièn bién bien'
		
		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta tiene acentos")

	def test_count_acents_unicode(self):

		str=u'bicicleta bicicletá hola bièn bién bien'
		
		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta tiene acentos")

	def test_count_upper_string(self):

		str='Bicicleta bicicleta Hola Bien biEn bieN BIEN'

		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',4)],"La lista devuelta tiene mayusculas")

	def test_count_upper_unicode(self):

		str=u'Bicicleta bicicleta Hola Bien biEn bieN BIEN'

		result=practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',4)],"La lista devuelta tiene mayusculas")

	def test_count_integer(self):
		with self.assertRaises(TypeError):
			practica.count(1)
	
	def test_count_float(self):
		with self.assertRaises(TypeError):
			practica.count(1.0)

	def test_count_emptyList(self):
		with self.assertRaises(TypeError):
			practica.count([])
	
	def test_count_list(self):
		with self.assertRaises(TypeError):
			practica.count(['test'])

#---Test_removeStopwords----------------------------------------------------------------------------------------------

	def test_remove_stopwords_empty(self):
		lstr=[]

		result=practica.remove_stopwords(lstr)
		
		self.assertEqual(result,[],"La lista devuelta no esta vacia")
	
	def test_remove_stopwords_strings(self):

		lstr=['yo','el','ella','tuyos','como','coche']

		result=practica.remove_stopwords(lstr)

		self.assertEqual(result,['coche'],"La lista devuelta tiene stopwords")

	def test_remove_stopwords_unicodes(self):

		lstr=[u'yo',u'el',u'ella',u'tuyos',u'como',u'coche']

		result=practica.remove_stopwords(lstr)

		self.assertEqual(result,['coche'],"La lista devuelta tiene stopwords")

	def test_remove_stopwords_integers(self):
		lstr=[1,2,3]
		result=practica.remove_stopwords(lstr)

		self.assertEqual(result,lstr,"La lista devuelta no es igual")

	def test_remove_stopwords_integers_ustopword(self):
		lstr=[1,2,3,u'que']
		result=practica.remove_stopwords(lstr)
		print(result)
		self.assertEqual(result,[1,2,3],"La lista devuelta es incorrecta")

	def test_remove_stopwords_integers_str_stopword(self):
		lstr=[1,2,3,'que']
		result=practica.remove_stopwords(lstr)

		self.assertEqual(result,[1,2,3],"La lista devuelta es incorrecta")

	def test_remove_stopwords_integer(self):
		lstr=1

		with self.assertRaises(TypeError):
			practica.remove_stopwords(lstr)

	def test_remove_stopwords_none(self):
		lstr=None

		with self.assertRaises(TypeError):
			practica.remove_stopwords(lstr)

#---Test_removeSymbolsAndWhiteSpaces----------------------------------------------------------------------------------------------

	def test_remove_symbols_and_whitespaces_string(self):
		lstr="que pasa ,tio, #, @ , (), (colega, bien,bien ©"

		result=practica.remove_symbols_and_whitespaces(lstr)
		
		self.assertEqual(result,["que" ,"pasa" ,"tio","colega","bien","bien"],"La lista devuelta tiene simbolos")

	def test_remove_symbols_and_whitespaces_unicode(self):
		lstr=u"que pasa ,tio, #, @ , (), (colega, bien,bien ©"

		result=practica.remove_symbols_and_whitespaces(lstr)

		self.assertEqual(result,["que" ,"pasa" ,"tio","colega","bien","bien"],"La lista devuelta tiene simbolos")

	def test_remove_symbols_and_whitespaces_integer(self):
		lstr=1

		with self.assertRaises(TypeError):
			practica.remove_symbols_and_whitespaces(lstr)
	
	def test_remove_symbols_and_white_spaces_none(self):
		lstr=None

		with self.assertRaises(TypeError):
			practica.remove_symbols_and_whitespaces(lstr)

	def test_remove_symbols_and_whitespaces_List(self):
		lstr=[]

		with self.assertRaises(TypeError):
			practica.remove_symbols_and_whitespaces(lstr)

#---Test_getWordsFrecuencies----------------------------------------------------------------------------------------------

	def test_get_words_frecuencies_strings(self):
		lstr=['hola','bicicleta','bicicleta','bien','bien','bien','bien']

		result=practica.get_words_frecuencies(lstr)
		print(result)
		self.assertEqual(result,[('hola',1),('bien',4),('bicicleta',2)],"La lista devuelta no es correcta")

	def test_get_words_frecuencies_unicodes(self):
		lstr=[u'hola',u'bicicleta',u'bicicleta',u'bien',u'bien',u'bien',u'bien']

		result=practica.get_words_frecuencies(lstr)
		print(result)
		self.assertEqual(result,[('hola',1),('bien',4),('bicicleta',2)],"La lista devuelta no es correcta")

	def test_get_words_frecuency_unicodes_strings(self):
		lstr=[u'hola','bicicleta',u'bicicleta','bien',u'bien','bien',u'bien']

		result=practica.get_words_frecuencies(lstr)
		print(result)
		self.assertEqual(result,[('hola',1),('bien',4),('bicicleta',2)],"La lista devuelta no es correcta")

	
	def test_get_words_frecuencies_string(self):
		lstr="test"

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)
	
	def test_get_words_frecuencies_unicode(self):
		lstr=u"test"

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_none(self):
		lstr=None

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_integers(self):
		lstr=[1,2,3]

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_string_integers(self):
		lstr=["test",1,2,3]

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_getWordsFrecuencies_Strings_Integer(self):
		lstr=["test","test2",3]

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_unicodes_integer(self):
		lstr=[u"test",u"test2",3]

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_unicode_integers(self):
		lstr=[u"test",1,2,3]

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)
	
	def test_get_words_frecuencies_empty(self):
		lstr=[]

		result=practica.get_words_frecuencies(lstr)

		self.assertEqual(result,[],"La lista devuelta no esta vacia")

	def test_get_words_frecuencies_unicode_integer(self):
		lstr=1

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)

	def test_get_words_frecuencies_special_character(self):
		lstr="©"

		with self.assertRaises(TypeError):
			practica.get_words_frecuencies(lstr)
