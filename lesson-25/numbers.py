import random as r

print("Keling o'ylangan sonni topish o'ynaymiz !")

def computer():
    print("1 dan 10 gacha son o'yladim . Topa olasizmi ?: ")
    k = r.randint(1,10)
    n = int(input(" >>> "))
    S = 0
    check(n, k , S)

def check(n , k , S):
    if n==k:
        S+=1
        print(f"TOPDINGIZ ! {k} sonini o'ylagan edim . {S} ta taxminda topdingiz ! TABRIKLAYMAN ! ✅♻️🥳")
        me()
    elif n>k:
        print("Xato ! Men o'ylagan son bundan kichikroq . Yana harakat qiling : ")
        n = int(input(" >>> "))
        S+=1
        check(n , k , S)
    else:
        print("Xato ! Men o'ylagan son bundan kattaroq . Yana harakat qiling : ")
        n = int(input(" >>> "))
        S+=1
        check(n , k , S)
def me():
    print("1 dan 10 gacha son o'ylang . Topishga harakat qilib ko'raman . ")
    text = input("Son o'ylagan bo'lsangiz istalgan tugmani bosing . ")
    S=0
    m = r.randint(1, 10)
    n = input(f"Siz {m} sonini o'yladingiz : Tog'ri (T) , men o'ylagan son bundan kattaroq (+) , yoki kichikroq (-) ishoralarini bosing : ")
    check2(m , n , S)



def check2(m , n ,S):
    if n=='T':
        S+=1
        print(f"TOPDIM ! Siz o'ylagan sonni {S} ta taxminda topdim  ! ✅♻️🥳")
        result()
    elif n=='-':
        b = m
        m = r.randint(1,b-1)
        n = input(f"Siz {m} sonini o'yladingiz : Tog'ri (T) , men o'ylagan son bundan kattaroq (+) , yoki kichikroq (-) ishoralarini bosing : ")
        S+=1
        check2(m , n ,S)
    elif n=='+':
        b = m
        m = r.randint(b+1, 10)
        n = input(f"Siz {m} sonini o'yladingiz : Tog'ri (T) , men o'ylagan son bundan kattaroq (+) , yoki kichikroq (-) ishoralarini bosing : ")
        S += 1
        check2(m , n ,S)

def result():
    pass
    print("Udare")
computer()



