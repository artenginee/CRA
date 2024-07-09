import sys


def get_award(n, board, userdata):
    conCnt = 0
    first_chance_done = [0] * 5
    second_chance_enable = [-1] * 5

    result = 0
    for user_char in userdata:
        # 2000 달러 찬스를 얻었는지 검사
        result += get2000points(board, second_chance_enable, user_char)
        result += get1000points(board, first_chance_done, second_chance_enable, user_char)

        passCnt = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == user_char:
                    passCnt += 1

        if passCnt >= 1:
            conCnt += 1
            result += (conCnt * 100) * passCnt
        else:
            conCnt = 0
            second_chance_enable = [-1] * 5

        flip_matching(board, user_char)

    return "$" + str(result)


def flip_matching(board, user_char):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == user_char:
                board[y][x] = '_'


def get1000points(board, first_chance_done, second_chance_enable, user_char):
    result = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != user_char:
                continue
            if first_chance_done[y] != 0:
                continue
            first_chance_done[y] = 1

            if x == 0:
                result += 1000
                second_chance_enable[y] = y

    return result


def get2000points(board, second_chance_enable, user_char):
    result = 0
    for y in range(len(board)):
        if second_chance_enable[y] != -1:
            for x in range(len(board[y])):
                if board[y][x] == user_char:
                    # 획득 성공시 2000달러를 얻는다.
                    result += 2000
                    break
            second_chance_enable[y] = -1
    return result