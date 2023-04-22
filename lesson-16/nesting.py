# car0 = {
#     "id" :123456789 ,
#     "model" : "Chevrolet",
#     "name" : "Malibu" ,
#     "color" : "black" ,
#     "speed" : 280 ,
#     "year" : 2022 ,
#     "km" :5000 ,
#     "price" : 32000
# }
#
# car1 = {
#     "id" :123456790 ,
#     "model" : "Chevrolet",
#     "name" : "Spark" ,
#     "color" : "black" ,
#     "speed" : 280 ,
#     "year" : 2022 ,
#     "km" :17000 ,
#     "price" : 8000
# }
#
# car2 = {
#     "id" :123456789 ,
#     "model" : "Chevrolet",
#     "name" : "Gentra" ,
#     "color" : "black" ,
#     "speed" : 280 ,
#     "year" : 2022 ,
#     "km" :12000 ,
#     "price" : 14000
# }
# cars = [car0 , car1 , car2]
# for car in cars:
#     for key , value in car.items():
#         print(f"{key} : {value}")
#     print("-----------------------")
#
# save = []
# for n in range(10):
#     cars = {
#         "id": 123456789,
#         "model": "Chevrolet",
#         "name": "Malibu",
#         "color": "black",
#         "speed": 280,
#         "year": 2022,
#         "km": 5000,
#         "price": 32000
#     }
#     save.append(cars)
#
# for malibu in save[5:]:
#     malibu['color']='white'
#
# for car in save:
#     if car["km"]==5000:
#         car["price"]=50000
#     else :
#         car["price"] = 40000
#
# for i in save:
#     print(i)
#


# dasturchilar ={
#     "ali": ["python" ,"c++"] ,
#     "otabek" : ["java" , "c#"],
#     "husan" : ["html" , "css"],
#     "ibrohim" : ["java" , "kotlin"] ,
#     "jahongir" :["python" , "sql"]
# }
#
# for name , language in dasturchilar.items():
#     print(f"\n {name.title()} quyidagi dasturlash tillarini biladi :")
#     for word in language:
#         print(word.upper())


