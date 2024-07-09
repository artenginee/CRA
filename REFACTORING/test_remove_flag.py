from unittest import TestCase

from REFACTORING.remove_flag import get_result


# 25+61=100
# 1 ~ 5자리수 덧셈 수식이 맞는지 확인하는 프로그램
# 띄어쓰기 없음
# str = "25+61=86"  # PASS
# str = "12345+12345=24690" # PASS
# str = "5++5=10" # ERROR
# str = "10000+1=10002" # FAIL

class Test(TestCase):
    def test_get_result(self):
        assert get_result("25+61=86") == 'PASS'
        assert get_result("12345+12345=24690") == 'PASS'
        assert get_result("5++5=10") == 'ERROR'
        assert get_result("10000+1=10002") == 'FAIL'

