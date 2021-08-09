import requests
from config import Config
from db import DBService
from Visitor import Visitor
import logging

class IpService:
    def __init__(self):
        self.__url = Config.IPSTACK_URL
        self.__key = Config.IPSTACK_KEY
        self.__db = DBService()

    def get_ip_info(self, ip_address):
        fields = 'ip,city'
        url = f'{self.__url}/{ip_address}?access_key={self.__key}'
        headers = {'content-type': 'application/json'}
        response = (requests.get(url, headers)).json()
        if 'error' in response:
            error = f"Error {response['error']['code']}: {response['error']['info']}"
            logging.error("Failed to fetch IP.", error)
            raise error
        else:
            visitor = Visitor(response['ip'], response['city'])
            self.__db.add_visitor(visitor)
            logging.info(f"Visitor {visitor} inserted successfuly")
            return response