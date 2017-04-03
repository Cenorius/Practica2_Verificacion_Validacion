# -*- coding: utf-8 -*-

from stop_words import get_stop_words
import re
import unicodedata

stopwords=get_stop_words('spanish')

def count(ustra):

	if(not isinstance(ustra, (str, unicode))):
		raise TypeError("The type must be str or unicode")

	#if the text's type is str converts to unicode
	if(isinstance(ustra, str)):
		ustra=unicode(ustra,'utf-8','ignore')

	#normalizes the text 
	ustra=unicodedata.normalize('NFKD', ustra).encode('ASCII', 'ignore')
	#converts to lowercase
	ustra=ustra.lower()
	
	la_words=removeSymbolsAndWhiteSpaces(ustra)
	la_words=removeStopwords(la_words)

	lcount=getWordsFrecuencies(la_words)
	#Order by: words's frequencies
	lcount=sorted(lcount,key=lambda x:x[1])
	
	return lcount

def remove_stopwords(la_words):
	la_words=[w for w in la_words if w not in stopwords ]

	return la_words

def remove_symbols_and_whiteSpaces(ustra):
	list=re.split('\W+',ustra)
	list=[w for w in list if (w is not '') and (w is not u'')]

	return list

def get_words_frecuencies(la_words):
	if(not isinstance(la_words, list)):
		raise TypeError("The type must be list")
	
	la_frecuencies=[]

	for w in la_words:
		if(not isinstance(w, (str, unicode))):
			raise TypeError("The list elements must be str or unicode")
		la_frecuencies.append(la_words.count(w))
	
	lcount=set(zip(la_words, la_frecuencies))
	lcount=list(lcount)

	return lcount
