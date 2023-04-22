from math import  sqrt

numbers = list(range(11))
# ildiz = list(map(sqrt , numbers))
# print(ildiz)


# def daraja2(x):
#
#     return x*x;
#
# print(list(map(daraja2 , numbers)))

# kvadratlar = list(map(lambda x : x*x , numbers))
# print(kvadratlar)

a = [4 , 5 ,6 , 7 , 8]
b = [21 , 12 , 14 , 9 , 2]
a_plus_b = list(map(lambda x , y : x+y , a , b))
print(a_plus_b)