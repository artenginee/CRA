from unittest import TestCase

from REFACTORING.split_sum import SplitSum


class TestSplitSum(TestCase):
    def setUp(self):
        self.sut = SplitSum()

    def tearDown(self):
        super().tearDown()

    def test_split_and_sum(self):
        ret = self.sut.split_and_sum("0-1-2-3-4-5")
        self.assertEqual(ret, 15)
