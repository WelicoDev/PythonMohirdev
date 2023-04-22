# import modul as cars
#
#
# car1 = cars.car_info('Chevrolet' , 'Malibu' , 'black' ,'automatic' , 2022 , 40000 )
# cars.info_print(car1)

from modul import *

car1 = car_info('Chevrolet' , 'Malibu' , 'black' ,'automatic' , 2022 , 40000 )
info_print(car1)


cars = car_input()

for car in cars :
    info_print(car)