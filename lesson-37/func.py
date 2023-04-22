def getArea(r , pi=3.1415916):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPeremetr(r , pi=3.1415916):
    """Doiraning peremetrini qaytaruvchi funksiya"""
    return 2*pi*r

print(getArea(5))
print(getPeremetr(5))