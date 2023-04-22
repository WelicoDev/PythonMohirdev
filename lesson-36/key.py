# KEYError

user = {
    "username" : "welico" ,
    "status" : "admin" ,
    "email" : "welico@gmail.com" ,
    "phone" : "+998942755638"
}

key = "tel"
try:
    print(f"Foydalanuvchi : {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas !")

print(user['username'])