class Visitor:
    def __init__(self,ip,city):
        self.__ip = ip
        self.__city = city
    
    def to_dict(self):
        return {'ip':self.__ip, 'city':self.__city}
    
    def get_ip(self):
        return self.__ip

    def get_city(self):
        return self.__city

    def __str__(self) -> str:
        return 'IP: {ip}, City: {city}'.format(ip = self.get_ip(), city=self.get_city())
