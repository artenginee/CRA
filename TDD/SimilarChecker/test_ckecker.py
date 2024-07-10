from unittest import TestCase, skip

from checker import SimilarChecker


class TestSimilarChecker(TestCase):

    def test_same_length(self):
        sut = SimilarChecker()
        self.assertEqual(60, sut.similar_cnt_point('A', 'A'))
        self.assertEqual(60, sut.similar_cnt_point('AAA', 'AAA'))
        self.assertEqual(60, sut.similar_cnt_point('AAAA', 'AAAA'))

    def test_more_than_twice(self):
        sut = SimilarChecker()
        self.assertEqual(0, sut.similar_cnt_point('A', 'AA'))
        self.assertEqual(0, sut.similar_cnt_point('A', 'AAA'))
        self.assertEqual(0, sut.similar_cnt_point('AA', 'AAAA'))
        self.assertEqual(0, sut.similar_cnt_point('AA', 'AAAAA'))
        self.assertEqual(0, sut.similar_cnt_point('AAAAA', 'AA'))

    def test_partial_score(self):
        sut = SimilarChecker()
        self.assertEqual(20, sut.similar_cnt_point('AAA', 'AAAAA'))
        self.assertEqual(30, sut.similar_cnt_point('AA', 'AAA'))
        self.assertEqual(20, sut.similar_cnt_point('AAAAA', 'AAA'))
