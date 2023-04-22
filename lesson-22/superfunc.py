# def avto_info(kompaniya , model , color , karobka , year , price= None):
#     avto = {
#         "kompaniya" : kompaniya ,
#         "model" : model ,
#         "color" : color ,
#         "karobka" : karobka ,
#         "year" :year ,
#         "price" : price
#     }
#     return  avto
#
# avto1 = avto_info("GM" , "Malibu" , "black" , "avtomat" , 2022)
# avto2= avto_info("GM" , "Gentra" , "white" , "mexanika" , 2020 , 15000)
# avtolar = [avto1 , avto2]
#
# print("Online bozorda mavjud avtomashinalar :")
# for avto in avtolar:
#     if avto['price']:
#         price = avto['price']
#     else:
#         price ="No'malum"
#
#     print(f"{avto['color'].title()} {avto['model'].title()} , {karobka} karobka  Price : {price}")


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi+=son
#     return  yigindi
#
# print(summa(1 , 2 , 3))
# print(summa(1 , 2 , 3 ,4 , 5 , 6 , 7))
# print(summa( 4 , 5 , 6 , 7 , 8 , 9 , 12 ))

# def summa(x , y , *sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
#     return x+y + sum(sonlar)
#
# print(summa(1 , 2 , 3))
# print(summa(1 , 2 , 3 ,4 , 5 , 6 , 7))
# print(summa(1 ,2 ,3 ,  4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ,12 ))

def avto_info(company , model , **info):
    """Avtomobil haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya """
    info['company'] = company
    info['model'] = model
    return  info

avto1 = avto_info("Chevrolet" , "Malibu" , year =2022 , color ="black" , price ="32000" , box="avtomatic")
print(avto1)
