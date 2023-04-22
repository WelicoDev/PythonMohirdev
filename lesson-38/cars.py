class Car:
    """(self , make , model ,year ,km=0 ,price=None)"""
    def __init__(self , make , model , year, km=0 ,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price

    def set_price(self ,price):
        self.price =price

    def add_km(self ,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km+=km
        else:
            raise ValueError("km manfiy bo'lishi mumkin ")

    def get_info(self):
        info = f"{self.make.upper()}  {self.model.title()}"
        info+=f"{self.year} - yil , {self.__km} km yurgan !"
        if self.price:
            info+=f" Narxi : {self.price}"
        return info


    def get_km(self):
        return self.__km


