class Game:
    def __init__(self):
        self.points = 0
        self.rolls = [0] * 21
        self.current_roll = 0

    # 기록하기
    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    # 점수계산
    def score(self):
        result = 0
        for i in range(self.current_roll):
            result += self.rolls[i]
        return result