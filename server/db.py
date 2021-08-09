from pymongo import MongoClient
from config import Config
from Visitor import Visitor
import logging

class DBService:
    def __init__(self):
        self.__client = MongoClient(Config.DB_URL)
        self.__db = self.__client[Config.DB_NAME]
        logging.info("Initiallized DB client successfuly")
    
    def add_visitor(self,visitor=Visitor):
        visitor_collection = self.__db['visitors']
        visitor_dict = visitor.to_dict()
        visitor_dict['_id'] = visitor.get_ip()
        res = visitor_collection.replace_one({'_id':visitor_dict['_id']}, visitor_dict, upsert=True)
        return res;

    def get_visitor(self,ip):
        visitor_collection = self.__db['visitors']
        res = visitor_collection.find({'ip':ip})
        return Visitor(ip, res['city'])
