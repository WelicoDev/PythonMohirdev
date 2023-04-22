def age():
    yosh = input("Yoshingizni kiriting : >> ")
    try:
        yosh = int(yosh)
    except ValueError23:
        print("Siz butun son kiritishingiz zarur!")
        age()
    else:
        print(f"Siz {2023 - yosh} - yilda tug'ilgansiz !")

age()

