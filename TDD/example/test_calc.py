import unittest

from TDD.example.calc import Calc


class MyTestCase(unittest.TestCase):
    def test_cal_minus(self):
        sut = Calc()
        self.assertEqual(sut.cal_minus(5,2), 3)
        self.assertEqual(sut.cal_minus(6, 1), 5)
        self.assertEqual(sut.cal_minus(1, 6), 5)

    def test_cal_fibo(self):
        sut = Calc()
        self.assertEqual(sut.fibo(1), 1)
        self.assertEqual(sut.fibo(2), 1)
        self.assertEqual(sut.fibo(3), 2)
        self.assertEqual(sut.fibo(4), 3)

if __name__ == '__main__':
    unittest.main()
