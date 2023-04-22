#ZeroDivisionError
x , y = 203 , 10
try :
    y/(x-5)
except ZeroDivisionError:
    print("o raqamiga bo'lish mumkin emas !")
else:
    print("y/(x-5) = " , y/(x-5))
