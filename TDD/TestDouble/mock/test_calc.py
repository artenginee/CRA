from unittest import TestCase
from unittest.mock import Mock, patch

from TDD.TestDouble.mock.calc import Cal


class TestCal(TestCase):
    def test_cal(self):
        # basic
        mk = Mock(spec=Cal)
        mk.get_sum.return_value = 10

        self.assertEqual(10, mk.get_sum(1, 2))
        print(mk.get_sum(1, 2))

        # side effect
        mk = Mock()
        mk.gogo.side_effect = TypeError

        with self.assertRaises(TypeError):
            mk.gogo()

        # custom function
        mk = Mock()

        def func(a, b):
            if a == 1 and b == 2:
                return 1000
            elif a == 2 and b == 3:
                return 2000
            elif a == 9 and b == 9:
                return 5000
            else:
                raise Exception

        mk.get_sum.side_effect = func

        self.assertEqual(1000, mk.get_sum(1, 2))
        self.assertEqual(2000, mk.get_sum(2, 3))
        self.assertEqual(5000, mk.get_sum(9, 9))

        with self.assertRaises(Exception):
            print(mk.get_sum(1, 100))

        # 호출 횟수 behavior
        mk = Mock()
        mk.size.return_value = 30

        mk.size()
        mk.size()
        mk.size()
        mk.size()

        self.assertGreaterEqual(mk.size.call_count, 2)
        self.assertLessEqual(mk.size.call_count, 5)

    @patch.object(Cal, 'say_hi', return_value='kfc')
    def test_sayhi(self, hi_mk):

        cal = Cal()
        print(cal.say_hi())

    @patch.object(Cal, 'get_sum', return_value=100)
    def test_sayhi(self, sum_mk):

        cal = Cal()
        print(cal.get_gop_three(1,2))
        print(sum_mk.call_count)
