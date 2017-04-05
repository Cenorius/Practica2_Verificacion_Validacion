# -*- coding: utf-8 -*-
import pymongo # pragma: no cover
from words_count import count

#'mongodb://localhost:27017/'
class data_base(object):

    URL_MONGO='mongodb://localhost:27017/'
    DATA_BASE_NAME='words'

    def __init__(self):
        self.db=pymongo.MongoClient(self.URL_MONGO)[self.DATA_BASE_NAME]


    def insert(self,dictionary):
        if(not self._exist(dictionary)):
            result=self.db.words.insert_one(dictionary).inserted_id
        else:
            result=None

        return result
    
    def get_words(self):
        iterator=self.db.words.find()
        list_text_words=[]

        for text_words in iterator:
            list_text_words.append(text_words)
        
        return list_text_words


    def delete(self,id):
        return self.db.words.delete_one({'_id': id})
    
    def update(self, dictionary,id):
        if type(dictionary) is not dict:
            raise TypeError

        return self.db.words.update_one({"_id" : id},{'$set':dictionary},False)


    def _exist(self, element):
        result = self.db.words.find_one(element)
        return result is not None


if __name__ == '__main__':
    dataB=data_base()
    tstr='bicicleta,bicicletá hola @bièn bién bien ©"'
    tstr2='bicicleta,bicicletá hola @bièn bien ©"'

    words2=count(tstr2)
    words=count(tstr)
    print words
    print words2

    id=dataB.insert(dict(words))
    print id

    print dataB.get_words()

    dataB.update(dict(words2),id)

    print dataB.get_words()

    print dataB.delete(id)




