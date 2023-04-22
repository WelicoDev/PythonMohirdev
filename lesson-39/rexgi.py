import re
from uzwords import words

# words1 ="тунлик"
# words2 ="тушлик"
# words3 ="туядек"
#
# andoza ="т....к$"
#
# print(re.match(andoza ,words1))
# print(re.match(andoza ,words2))
# print(re.match(andoza ,words3))
#
# matches =[]
# for word in words:
#     if re.match(andoza ,word):
#         matches.append(word)
#
# print(matches)
#
# #Emailni ajratib olish
#
# text ="Facebook is  xurramovotabek568@gmail.com showing information to help you better understand the purpose of a Page. See actions taken by the people who manage and post content. "
#
# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza ,text)
#
# print(email)
# Kuchli parolni tekshirish
msg ="Yangi parol kiriting "
msg+="(kamida 8 belgidan iborat , kamida 1 ta lotin bosh harf , 1ta kichik harf ,)"
msg+= "1 ta son va 1 ta maxsus belgidan iborat bo'lishi kerak ) :"
andoza ="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"

while True:
    password = input(msg)
    if re.match(andoza , password):
        print("Maxfiy parol qabul qilindi !")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi !")


