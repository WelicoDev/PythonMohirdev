# INDEXError

mevalar = ['olma' , 'anor' , 'nok' , 'banan' , 'apelsin' , 'xurmo']
n = int(input("Ro'yxatdagi nechanchi meva kerak : >> "))
try :
    mevalar[n]
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva mavjud \n Siz mavjud bo'lmagan index raqam kiritdingiz !")
else:
    print(mevalar[n])