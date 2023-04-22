import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car classini tekshirish uchun test !"""
    def setUp(self):
        make ="GM"
        model ="Malibu"
        year = 2022
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make , model , year)
        self.avto2 = Car(make , model , year , price=self.price)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshirdik
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone methodi bilan tekshirdik
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals methodi bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narxini tekshiramiz
        self.assertEqual(self.price , self.avto2.price)
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price , self.avto2.price)

    def test_add_km(self):
        """Musbat qiymat berib ko'ramiz !"""
        self.avto1.add_km(self.km)
        self.assertEqual(self.km , self.avto1.get_km())
        # Manfiy qiymat berib ko'ramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error) , ValueError)

unittest.main()