import random

def son_top(x=10):
    tasodifiy_son = random.randint(1 , x)
    print(f"Men 1 dan {x} gacha son o'yladim . Topa olasizmi ? : ")
    S = 0
    while True:
        taxmin = int(input(" >>> "))
        if taxmin < tasodifiy_son :
            S+=1
            print("Xato men o'ylagan son bundan kattaroq . Yana harakat qiling : ")

        elif taxmin > tasodifiy_son :
            S+=1
            print("Xato men o'ylagan son bundan kichikroq . Yana harakat qiling : ")
        else :
            S+=1
            break
    print("Tabriklayman ! TOPDINGIZ ✅♻️🥳")
    print(f"Siz  men o'ylagan sonni {S} ta taxminda topdingiz !")


    return S


def sontop_pc(x = 10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing . Men topaman .")
    quyi = 1
    yuqori = x
    M =0
    while True:
        M+=1
        if quyi != yuqori :
            taxmin =  random.randint(quyi , yuqori)
        else:
            taxmin = quyi
        reply = input(f" Siz {taxmin} sonini o'yladingiz : tog'ri (T) ,"
                      f"men o'ylagan son bundan kattaroq (+) , yoki kichikroq (-) ".lower())
        if reply =='-':
            yuqori = taxmin -1
        elif reply == '+':
            quyi = taxmin +1
        else:
            break
    print(f"Men siz o'ylagan sonni {M} ta taxmin bilan topdim  !")

    return M

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user > taxminlar_pc:
            print("Men yutdim !")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz !")
        else:
            print("Durrang !")

        yana = int(input("Yana o'ynaysizmi ? :  Yes (1) / No (0) :"))

play()