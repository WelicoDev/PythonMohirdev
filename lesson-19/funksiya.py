# Funksiyalar
# author : Otabek


# def welcome():
#     name ="Otabek"
#     print(f"Assalom aleykum  {name} !")
#
#
# def info():
#     name ="Otabek"
#     age =18
#     print(f"{name} siz {age} yoshdasiz !")
#
#
# def next():
#     name ="Otabek"
#     print(f"{name} siz TATU talabasisiz  !")
#
#
# def help():
#     name ="Otabek"
#     print(f" {name}  sizga nima yordamim kerak !")
#
# class menu():
#     print("1. welcome ")
#     print("2. info ")
#     print("3.  next ")
#     print("4.  help ")
#     n = int(input("Kerakli sahifani tanlang : >>> "))
#     if n==1:
#         welcome()
#     elif n==2:
#         info()
#     elif n==3:
#         next()
#     elif n==4:
#         help()
#     else:
#         print("Bu raqamdagi menu mavjud emas ! \n Iltimos qayta urining !")
#         menu()
#
# menu()

# def welcome(name):
#     """ Foydalanuvchilarnu kutib oluvchi funksiya """
#     print(f"Assalom aleykum {name}")
#
# base = ["Otabek" , "Habib" , "Islom" , "javohir"]
# for name in base:
#     welcome(name)
#
# print(welcome.__doc__)

# def fullname(first_name , last_name):
#     """ Ism familya ro'yxati !"""
#     print(f"Foydalanuvchi ismi : {first_name} \n"
#           f"Foydalanuvchi familyasi : {last_name}")
#
# first_name ="Otabek"
# last_name = "Xurramov"
# fullname(first_name ,last_name)

def year(name , yil):
    """ Yoshni hisoblash """
    print(f" Hurmatli {name} sizning yoshingiz {2022-yil} da")
year("Jahongir" , 2003)