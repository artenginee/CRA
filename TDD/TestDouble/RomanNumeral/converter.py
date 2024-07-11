class RomanConverter:
    def __init__(self):
        self.table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

    def convert(self, roman_num: str) -> int:
        result = 0
        for i in range(len(roman_num) - 1):
            if self.table[roman_num[i]] < self.table[roman_num[i + 1]]:
                result -= self.table[roman_num[i]]
            else:
                result += self.table[roman_num[i]]

        result += self.table[roman_num[-1]]
        return result