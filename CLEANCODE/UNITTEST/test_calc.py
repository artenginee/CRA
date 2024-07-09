from unittest import TestCase

from calc import Calc


class TestCalc(TestCase):
    def test_get_sum(self):
        sut = Calc()  # 준비 system under test
        ret = sut.get_sum(1, 2)  # 실행
        self.assertEqual(ret, 3)  # 검증

    def test_get_sum_negative(self):
        sut = Calc()
        ret = sut.get_sum(-1, -2)
        self.assertEqual(ret, -3)

    def test_get_abs_sum_pos(self):
        sut = Calc()
        ret = sut.getAbsSum([1, 2, 3])
        self.assertEqual(ret, [1, 2, 3])

    def test_get_abs_sum_neg(self):
        sut = Calc()
        ret = sut.getAbsSum([-1, -2, -3])
        self.assertEqual(ret, [1, 2, 3])

    def test_get_abs_sum_zero(self):
        sut = Calc()
        ret = sut.getAbsSum([0, 0, 0])
        self.assertEqual(ret, [0, 0, 0])

    def test_get_abs_sum_mix(self):
        sut = Calc()
        ret = sut.getAbsSum([-1, 2, 0])
        self.assertEqual(ret, [1, 2, 0])