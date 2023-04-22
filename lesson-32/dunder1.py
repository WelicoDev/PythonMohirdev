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

    def __str__(self):
        return  f"Avto : {self.model} , Make : {self.make} , color : {self.color}"

    def __eq__(self, y):
        return self.price==y.price

    def __lt__(self, y):
        return self.price<y.price

    def __le__(self, y):
        return self.price<=y.price

avto = Auto("GM" , 'Malibu' , 'black' , 2023 , 40000 , 1200)
avto1 = Auto("GM" , 'Cobalt' , 'white' , 2022 , 15000 , 9200)
avto2 = Auto("GM" , 'Gentra' , 'black' , 2022 , 15000 , 9200)
avto3 = Auto("GM" , 'Kaptiva' , 'white' , 2023 , 30000 , 4000)

print(avto)
x,y = 10 , 20
print(x>y)
print(avto1==avto2)
print(avto1<avto3)
print(avto<=avto3)
print(avto>=avto3)

class AvtoSalon:
    """AvtoSalon classi"""
    def __init__(self , name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, key, value):
        self.avtolar[key]=value

    def add_avto(self , *qiymat):
        for avto in qiymat:
            if isinstance(avto , Auto):
                self.avtolar.append(avto)
            else:
                print("Avtoni kiriting :")

salon1 = AvtoSalon("MaxAuto")
salon1.add_avto(avto1 , avto2 , avto3)
print(isinstance(salon1,AvtoSalon))
print(salon1[0])
print(salon1[2])
