
#
# numbers = r.sample(range(100) , 10)
# print(numbers)
#
# def juftmi(x):
#     return x%2==0

#
# juft_numbers = list(filter(juftmi , numbers))
# print(juft_numbers)
#
# juft_numbers = list(filter(lambda x : x%2==0 , numbers))
# print(juft_numbers)

message = 'Python is fun'

# check if the message starts with Python
print(message.startswith('Python'))

fructics = ['olma' , 'anor' , 'banan' , 'shaftoli' , 'o\'rik' , 'tarvuz' , 'qovun' , 'uzum' , 'nok' , 'behi' , 'bodom']
harf = 'b'
fructic_b = list(filter(lambda meva : len(meva)<=4 , fructics))
print(fructic_b)