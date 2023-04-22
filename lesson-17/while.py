# name = input("Isming nima : ")
# savol = f"Salom , {name} . \n Xush kelibsiz ! \n Nechi yoshsiz ? >> "
# yosh = int(input(savol))
# height = input("Bo'yingiz necha metr ?")
# height = float(height)
#
# print(f"Mening ismim {name} , yoshim {yosh} da , bo'y uzunligim {height} sm.")

# number = 1
# while number<=5:
#     print(number , end='  ')
#     number+=1
#
# print("Dastur tugadi")
#

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur !")
# savol = "Istalgan son kiriting : >> "
# savol+= "( dasturni to'xtatish uchun 'exit' deb yozing !) : "
# qiymat = []
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#
# print("Dastur tugadi !")

# ishora

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur .")
# savol = "Istalgan son kiriting : "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing !) >> "
# ishora=True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else :
#         print(float(qiymat)**2)
#
# print("Dastur to'xtadi !")

# break
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur .")
# savol = "Istalgan son kiriting : "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing !) >> "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else :
#         print(float(qiymat)**2)
#
# print("Dastur to'xtadi !")

# for break

# numbers = list(range(1,11))
# for i in numbers :
#     if i==5 :
#         break
#     else:
#         print(f"{i} ning kvadrati {i**2} ga teng !")

# contunie

# numbers = list(range(1,11))
# for i in numbers :
#     if i==5 :
#         continue
#     print(f"{i} ning kvadrati {i**2} ga teng !")

# while contunue

son =0
while son<10 :
    son+=1
    if son%2!=0:
        continue
    else :
        print(son)