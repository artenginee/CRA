from unittest import TestCase

from converter import RomanConverter


class TestRomanConverter(TestCase):
    def test_roman_one_char(self):
        lst = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]
        for roman_num, arabic_num in lst:
            with self.subTest(f'{roman_num} 는 {arabic_num}이다'):
                converter = RomanConverter()
                self.assertEqual(arabic_num, converter.convert(roman_num))

    def test_roman_multi_char(self):
        lst = [
            ('II', 2),
            ('III', 3),
            ('VI', 6),
            ('XI', 11),
            ('IV', 4),
            ('IX', 9),
        ]
        for roman_num, arabic_num in lst:
            with self.subTest(f'{roman_num} 는 {arabic_num}이다'):
                converter = RomanConverter()
                self.assertEqual(arabic_num, converter.convert(roman_num))