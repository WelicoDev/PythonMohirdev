student = {
    'name' :'Otabek',
    'age' : 18,
    'study':'TUIT',
    'course' : 2,
    'interest':'programming'
}

print(student.items())

for key, value in student.items():
    print(f"{key}:{value}")

    # talaba={
#     'surname':'Xurramov',
#     'name':'Otabek',
#     'age':18,
#     'interests':'programming',
#     'study':'TATU',
#     'fakultet':'DIF',
#     'course':2
# }
# print(talaba['study'])

# print(talaba.items())
# for value in talaba.items():
#     print(value)
# for key,value in talaba.items():
#     print(f"Kalit :{key}")
#     print(f"Qiymat :{value} \n")

# telfonlar={
#     'Otabek':'Redmi note 9 pro',
#     'Islom':'Iphone 6+',
#     'Sarvar':'Redmi note 11 pro',
#     'Zohidjon':'Galaxy S10+ 5g',
#     'Doniyor':'Iphone x',
#     'Ozodbek':'Honor 50x',
#     'Habibullo':'Iphone x',
#     'Jahongir':'Iphone 6+'
# }
# for key ,value in telfonlar.items():
#     print(f"{key.title()} ning telfoni {value} !")

# fructic ={
#     'olma':10000,
#     'apelsin':20000,
#     'nok':15000,
#     'uzum':8000,
#     'bodom':90000,
#     'xurmo':14000,
#     'banan':18000
# }

# for item in fructic.keys():
#     print(item)
# print("Do\'kondagi mahsulotlar :")
# for meva in fructic.keys():
#     print(meva.title())

# print("Do\'kondagi mahsulotlar :")
# for meva in fructic:
#     print(meva.title())

# bozorlik = ['anor' , 'non' , 'shakar' , 'banan', 'baliq' , 'uzum' , 'yog\'','go\'sht','bodring']
# for mahsulot in fructic:
#     if mahsulot in bozorlik :
#         print(f"{mahsulot.title()} ning narxi {fructic[mahsulot]} so'm ")

# for buyum in bozorlik :
#     if buyum not in fructic:
#         print(f"Iltimos , do'koningizga {buyum} ham olib keling !")

# print("Bozorliklar ro'yxati :")
# for item in sorted(bozorlik):
#     print(item.title())

# for item in telfonlar.values():
#     print(item)

# print("Foydalanuvchilar quyidagi telfonlardan foydalanishadi :")
# for phone in set(telfonlar.values()):
#     print(phone)

toys = { 'bear' , 'suv pistalet' , 'qo\'g\'irchoq' , 'shashka' , 'shahmat'}
print(toys)