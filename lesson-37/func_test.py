import unittest
from func import getArea ,getPeremetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5) , 78.53979)
    def test_peremetr(self):
        self.assertAlmostEqual(getPeremetr(5) ,31.415916)

unittest.main()