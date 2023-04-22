# def create_fullname(first_name , last_name):
#     fullname = f"{first_name}  {last_name} ."
#     return  fullname
#
# first_name = "Otabek"
# last_name ="Xurramov"
# name = create_fullname(first_name , last_name)
# print("Name : " , name)

# def create_fullname(first_name , last_name , father_name = " "):
#     fullname = f"{first_name}  {last_name} {father_name}."
#     return  fullname.title()
#
# first_name = input("Ismingizni kiriting : >> ")
# last_name =input("Familyangizni kiriting : >> ")
# father_name = input("Otangizni ismini kiriting : >> ")
# name = create_fullname(first_name , last_name , father_name)
# print("Name : " , name)

def avto_info(kompaniya , model , color , karobka , year , price):
    avto = {
        "kompaniya" : kompaniya ,
        "model" : model ,
        "color" : color ,
        "karobka" : karobka ,
        "year" :year ,
        "price" : price
    }
    return  avto
#
# print("Avtomobil haqia ma'lumotlarni kiriting !")
# kompaniya = input("Kompaniya nomini kiriting : >> ")
# model = input("Model nomini kiriting : >> ")
# color = input("Rangini kiriting : >> ")
# karobka =input("Karobkasi nomini kiriting : >> ")
# year = int(input(" Yilini kiriting : >> "))
#
# car = avto_info(kompaniya , model , color , karobka , year )
# print(" CAR name : " , car)

# def oraliq(min , max , qadam):
#     sonlar =[]
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
#
# numbers = oraliq(1 , 20 ,2)
# numbers = oraliq(100 , 200 , 5)
# print(numbers)

print("Salondagi avtomoshinalar ro'yxatini shakllantiramiz .")
cars = []
while True:
    print("\n Quyidagi malumotlarni kiriting :\n " , end='')
    kompaniya = input("Kompaniya nomini kiriting : >> ")
    model = input("Model nomini kiriting : >> ")
    color = input("Rangini kiriting : >> ")
    karobka = input("Karobkasi nomini kiriting : >> ")
    year = int(input(" Yilini kiriting : >> "))
    price = input("Narxini kiriting : >> ")

    cars.append(avto_info(kompaniya, model, color, karobka, year , price))

    reply = input("Yana avtomobil qo'shasizmi ? ( yes / no ) ")

    if reply == "no":
        break

print("Salonimizdagi avtolar : ")
for avto in cars:
    if avto['price']:
        price = avto['price']
    else:
        price ="No'malum"

    print(f"{avto['color'].title()} {avto['model'].title()} , {karobka} karobka  Price : {price}")