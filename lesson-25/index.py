n, m = map(int, input().split())
k='_'
x , y , y1 , x1 = 0 , 1 , 0 , 0
welicodev = [[0] * m for k in range(n)]
for i in range(1, n * m + 1):
    welicodev[x1][y1] = i
    if welicodev[(x + x1) % n][(y + y1) % m]:
        x, y = y, -x
    x1 += x
    y1 += y    
for welico in welicodev:
    print(*(f'{a:<3}' for a in welico), sep='')

# 1-masala
