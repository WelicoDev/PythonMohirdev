# Author : Welico Developer

# Object oreint programming and Class

# x = 10
# print(type(x))
#
# text = "assalom aleykum"
# print(type(text))
#
# print(text.upper())

# def hello():
#     print("Hello World !")
#
# print(type(hello))
# hello()

class Student():
    def __init__(self , first_name , last_name , age , profession , study , course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.study = study
        self.course = course

    def name(self):
        return  self.first_name

    def last_name(self):
        return self.last_name

    def age_year(self, year):
        return year - self.age

    def welcome(self):
        return  f"Assalom aleykum {self.first_name} {self.last_name} yoshingiz {self.age} . "

talaba = Student("Otabek" , "Xurramov" , 19 , "" , "TUIT" , 2)

print(talaba.age_year(2023))