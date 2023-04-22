import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_full_name(self):
        name = get_full_name('alijon','valiyev','rustamovich')
        self.assertEqual(name,'Alijon Valiyev Rustamovich')


unittest.main()
