# son =int(input("Sonni kiriting >>> "))
# if son>0:
#     print("Musbat")
# elif son==0:
#     print("Son nolga teng")
# else:
#     print("Manfiy")

# yosh =int(input("Yoshingizni kiriting >>> "))
# if yosh<=4:
#     narx=0
# elif yosh<=12:
#     narx=5000
# elif yosh>70:
#     narx=0
# else:
#     narx=10000
# print(f"Sizga kirish {narx} so'm !")

# today=input("Bugun qanday kun ?")
# if today.lower()=="shanba" or today.lower()=="yakshanba":
#     print("BUgun dam olish kuni !")
# else:
#     print("Bugun ish kuni !")

# day = str(input("Bugun haftani qaysi kuni ? >>>"))
# temperatura = int(input("Harorat necha gradus ?"))

# if day.lower()=="yakshanba" and temperatura>35:
#     print("Cho'milgani kettik !")
# elif day.lower()=="shanba" and temperatura>30:
#     print("Futbol o'ynagani kettik !")
# else:
#     print("Darsga kettik !")

# if (day.lower()=="yakshanba" or day.lower()=="shanba") and temperatura>35:
#     print("Cho'milgani kettik !")
# else:
#     print("Darsga kettik !")

# narx = 15000
# choy =True
# salat =False
# kampot =True
# non=True
# assarti =False

# if choy:
#     print("Mijoz choy sotib oldi !")
#     narx=narx+3000
# if salat:
#     print("Mijoz salat sotib oldi !")
#     narx=narx+5000
# if kampot:
#     print("Mijoz kampot sotib oldi !")
#     narx=narx+8000
# if non:
#     print("Mijoz non sotib oldi")
#     narx=narx+3000
# if assarti:
#     print("Mijoz assarti sotib oldi !")
#     narx=narx+6000

# print(f"Mijoz kassaga {narx} so'm to'lov qilasiz !")

# menu =['manti','somsa','osh','xonim','mastava','shashlik','qozonkabob','halim']
# print('mastava' in menu)

# ovqat=input("Nima ovqat yeysiz ? >>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi !")
# else:
#     print("Afsuski bizda bu ovqat yuq !")

# ovqat=input("Nima ovqat yeysiz ? >>>")
# if ovqat.lower() not in menu:
#     print("Bu ovqat bizda mavjud emas ! !")
# else:
#     print("Buyurma bo'yicha ovqat yetkaziladi !")

menu =["somsa","shashlik","qozonkabob","galubsi","osh","salat","non","pepsi","kola"]
buyurmalar=[]
n=int(input("Nechta ovqat buyurma qilasiz ?"))
while n>0 :
    ovqat=input('Ovqatni nomini kiriting >>>')
    n-=1
    buyurmalar.append(ovqat)

if buyurmalar:
    for taom in buyurmalar:
        if taom in menu:
            print("Buyurmangiz qabul qilindi !")
        else:
            print(f" Kechirasiz ! Menuda bu {taom} yuq !")
else:
    print('Buyurmalar mavjud emas !')

        
    