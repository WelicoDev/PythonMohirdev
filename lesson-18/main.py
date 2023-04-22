# print("Yaqin do'stlaringizni ro'yxatini tuzamiz !")
# name = []
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting : >> "
#     ism = input(savol)
#     name.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi ? (ha / yo'q ) \n >>> ")
#     n+=1
#     if takrorlash !='ha':
#         break


# dostlar = {}
# ishora = True
# while ishora :
#     ism = input(" Do'stingizni ismini kiriting : ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting : >> ")
#     dostlar[ism] = int(yosh)
#
#     javob = input(" Yana ma'lumot qo'shasizmi ?  (ha / yo'q ) ")
#     if javob == "yo'q":
#         ishora =False
# for ism , yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# cars = ['lasseti' , 'malibu' , 'nexia' , 'orlando' , 'gentra' , 'cobalt']
# while 'nexia' in cars:
#     cars.remove("nexia")
#
# print(cars)

# cars = ['lasseti' , 'malibu' , 'nexia' , 'orlando' ,'nexia', 'gentra' , 'cobalt' , 'nexia']
# while 'nexia' in cars:
#     cars.remove("nexia")
#
# print(cars)

talabalar = ['hasan' , 'islom' , 'javohir' , 'murod' , 'otabek']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting : ")
    print(f"{talaba.title()} baholandi !")
    baholangan_talabalar[talaba] = int(baho)

print(baholangan_talabalar)