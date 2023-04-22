# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()
# print(type(file))

# with open('pi.txt') as file:
#     pi = file.read()
#
#
pi=pi.rstrip()
pi = pi.replace('/n' , '')
#
#
# print(pi)
# print(type(pi))

# filename = 'date/students.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
# with open(filename) as file:
#     talabalar = file.readlines()
#
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# filename = 'newfile.txt'
# name = 'Otabek Xurramov'
# birthday =2004
# with open(filename , 'w') as file:
#     file.write(name)
#     file.write(str(birthday))

# filename = 'new_file.txt'
# name = 'Otabek Xurramov'
# birthday =2004
# with open(filename , 'a') as file:
#     file.write(name+'\n')
#     file.write(str(birthday)+'\n')
#
import pickle

# student1 = {'name':'Otabek' , 'last_name':'Xurramov' , 'birthday':2004 , 'study':'TUIT' , 'course':2}
# student2 = {'name':'Javohir' , 'last_name':'Namazov' , 'birthday':2003 , 'study':'TUIT' , 'course':2}
#
# with open('info' , 'wb') as file:
#     pickle.dump(student1 , file)
#     pickle.dump(student2 , file)

with open('info' , 'rb') as file:
    student1 = pickle.load(file)
    student2 = pickle.load(file)

print(student1)
print(student2)