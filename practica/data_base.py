# -*- coding: utf-8 -*-
import pymongo


#'mongodb://localhost:27017/'
class data_base(object):

    URL_MONGO='mongodb://localhost:27017/'
    DATA_BASE_NAME='words'

    def __init__(self):
        self.db=pymongo.MongoClient(self.URL_MONGO)[self.DATA_BASE_NAME]


    def insert(self,dictionary):

        if(not self._exist(dictionary)):
            result=self.db.words.insert_one(dictionary)
        else:
            result=None

        return result is not None
    
    def get_words(self):
        iterator=self.db.words.find()
        list_text_words=[]

        for text_words in iterator:
            list_text_words.append(text_words)
        
        return list_text_words


    def delete(self,id):

        self.db.words.remove({'_id': id})
    
    def update(self, dictionary,id):
        self.db.words.update_one({"_id" : id},{'$set':dictionary},False)


    def _exist(self, element):
        result = self.db.words.find_one(element)
        return result is not None

    def _alive(self):
        """Siempre tiene que estar alive por lo tanto siempre se devuelve True
        """

        return True