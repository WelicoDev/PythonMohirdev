import random

n=100
numbers = list(range(1 , n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)
# number2 = list(range(1 ,n+1))
# print(sum(number2)-sum(numbers))

# for i in range(1 , n):
#     if i not in numbers:
#         print(i)
#         break

summa = n*(n+1)/2
print(summa-sum(numbers))