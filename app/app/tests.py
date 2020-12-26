from django.test import TestCase
from app.calc import add_num

class CalcTest(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_num(3, 8), 11)
