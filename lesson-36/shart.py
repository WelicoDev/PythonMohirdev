while True:
    yosh = input("Yoshingizni kiriting : >> ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2023-yosh}-yilda tug'ulgansiz !")