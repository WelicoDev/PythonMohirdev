from uuid import uuid4
class Auto:
    """Avtomobil classi"""
    __num_avto =0
    def __init__(self , make , model , color , year , price , km ):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()

        Auto.__num_avto+=1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Mashinaning kmga yana km qo'shish"""
        if km>=0:
            self.__km+=km
        else:
            print("Mashina km kamaytirib bo'lmaydi !")