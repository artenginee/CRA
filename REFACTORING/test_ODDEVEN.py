from unittest import TestCase

from REFACTORING.ODDEVEN import OddEven


class TestOddEven(TestCase):
    def setUp(self):
        self.sut = OddEven()

    def tearDown(self):
        super().tearDown()

    def test_get_result(self):
        self.assertEqual(self.sut.get_result([1,2,3,0]), ['X', 'O', 'X','O'])

    def test_all_odd(self):
        ret = self.sut.get_result([1,3,5])
        self.assertEqual(ret, None)

    def test_all_even(self):
        ret = self.sut.get_result([2,4,6])
        self.assertEqual(ret, None)