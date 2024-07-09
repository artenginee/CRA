def get_result(str):
    # +와 = 개수 확인

    plus_cnt = count_of('+', str)
    plus_index = index_of('+', str)
    equal_cnt = count_of('=', str)
    equal_index = index_of('=', str)

    # 가드절 추출하기
    if not is_valid_char(str) :
        return "ERROR"
    if plus_cnt != 1 or equal_cnt != 1 :
        return "ERROR"
    if plus_index < 1 or equal_index < 3 or len(str) - 1 <= equal_index or equal_index <= plus_index :
        return "ERROR"

    num1 = int(str[0:plus_index])
    num2 = int(str[plus_index + 1:equal_index])
    num3 = int(str[equal_index + 1:])

    if num1 + num2 == num3:
        return "PASS"
    else:
        return "FAIL"


def is_valid_char(str):
    for i in range(len(str)):
        if str[i] == "+":
            continue
        elif str[i] == "=":
            continue
        elif not str[i].isdigit():
            return False
    return True


def index_of(op, str):
    result = 0
    for i in range(len(str)):
        if str[i] == op:
            result = i
    return result


def count_of(op, str):
    result = 0
    for i in range(len(str)):
        if str[i] == op:
            result += 1
    return result