import  math

# uzunlik = lambda pi , r : 2*pi*r
# print(uzunlik(math.pi ,10))
#
# daraja = lambda x , y : x**y
# print(daraja(2 , 9))

def daraja(n):
    return lambda x: x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(kub)
print(daraja(3))
kvadrat = daraja(2)
print(kvadrat(4))
kub = daraja(3)
print(kub(6))