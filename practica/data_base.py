# -*- coding: utf-8 -*-
import pymongo

#'mongodb://localhost:27017/'
class data_base(object):
    def __init__(self,url_mongo,data_base_name):
        self.url_mongo=url_mongo
        self.data_base_name=data_base_name

    def insert(self,dictionary):
        db=pymongo.MongoClient(self.url_mongo)[self.data_base_name]
        db.words.insert_one(dictionary)
    
    def get_words(self):
        db=pymongo.MongoClient(self.url_mongo)[self.data_base_name]

        iterator=db.words.find()
        list_text_words=[]

        for text_words in iterator:
            list_text_words.append(text_words)
        
        return list_text_words


    def delete(self,id):
        db=pymongo.MongoClient(self.url_mongo)[self.data_base_name]
        db.words.remove({'_id': id})
    
    def update(self, dictionary,id):
        db=pymongo.MongoClient(self.url_mongo)[self.data_base_name]
        db.words.update_one({"_id" : id},{'$set':dictionary},False)


    def _exist(self, element):
        db=pymongo.MongoClient(self.url_mongo)[self.data_base_name]
        result = db.words.find_one(element)
        return element is not None