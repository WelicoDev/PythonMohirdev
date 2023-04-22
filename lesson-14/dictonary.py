# car ={'model':'malibu' , 'color' : 'black'}
# print(car['model'])
# print(car['color'])

# translate = {'apple':'olma' , 'orange':'apelsin' , 'banana':'banan'}
# print(translate['banana'])
# print(f"Men kecha uyga 2 kg {translate['apple']} olib keldim")


# talaba = {'name':'Otabek' , 'age':18 , 'gender':'male' , 'birthday':'27-05-2004' , 'height': 182 }

# print(f"Men {talaba['age']} yoshdaman va mening bo'y uzunligim {talaba['height']} sm")

# talaba['study']='TUIT'
# talaba['course'] = 2
# talaba['name'] ='Javohir'
# del talaba['gender']
# print(talaba)

telefonlar = {
    'ali' :'iphone x',
    'hasan': 'redmi',
    'javohir':'oppo',
    'husan':'samsung'
}
# print(telefonlar['ali'])

phone = telefonlar.get('otabek' , 'Bunday foydalanuvchi yoq')
print(phone)