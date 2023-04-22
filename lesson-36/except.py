n = input("Butun son kiriting : >> ")
try:
    n = int(n)
    x = 20/n
except ValueError:
    print("Butun son kiritmadingiz !")
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi !")
else:
    print(f"x = {x}")