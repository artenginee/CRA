from unittest import TestCase

from REFACTORING.Calc import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        print('Before..')
        self.sut = Calculator()

    def tearDown(self):
        print('After..')

    def test_get_sum(self):
        ret = self.sut.get_sum(1,2)
        self.assertEqual(ret, 3)

    def test_get_sum2(self):
        ret = self.sut.get_sum(1,1)
        self.assertEqual(ret, 2)


