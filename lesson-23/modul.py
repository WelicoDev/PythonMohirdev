def car_info(company , model , color , box , year , price = None):
    """Avtomobil ro'yxatini lug'at ko'rinishida qaytaruvchi funksiya"""
    car = {
        'company': company ,
        'model': model,
        'color': color ,
        'box' : box ,
        'year' : year ,
        'price' : price
    }
    return car

def car_input():
    """Foydalanuvchiga car_info funksiyasi yordamida avtomobil haqida ma'lumotlarni kiritib beradi """
    cars = []
    while True:
        print("\n Quyidagi ma'lumotlarni kiriting : " , end='')
        company = input("Company name : >> ")
        model = input("Model name : >> ")
        color = input("Color : >> ")
        box = input("Box name : >> ")
        year = int(input(" Year of manufacture : >> "))
        price = int(input(" Enter the price : >> "))

        cars.append(car_info(company , model , color , box , year , price))

        reply = input("\n Would you like to add another car ? (yes/no) : >> ")
        if reply=='no':
            break
    return cars

def info_print(car_info):
    """Avtomobillar haqida saqlangan lug'atni ekranga chiqarish !"""
    print(f" Color : {car_info['color'].title()} \n Company :  {car_info['company'].upper()}\n"
          f" Model : {car_info['model'].upper()} \n Box :  {car_info['box'] }\n"
          f" Year : {car_info['year']}  \n  Price : {car_info['price']} ")

