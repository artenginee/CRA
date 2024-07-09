class SplitSum:
    def split_and_sum(self, text: str):
        if (not isinstance(text, str)) or len(text) == 0:
            return 0

        values = text.split("-")
        result = 0
        result = self.check_digit(values)

        return result

    def check_digit(self, values):
        if not self.is_all_digit(values):
            return 0

        return self.get_sum(values)

    def is_all_digit(self, values):
        for i in range(len(values)):
            if not values[i].isdigit():
                return False
        return True

    def get_sum(self, values):
        ret = 0
        for i in range(len(values)):
            ret += int(values[i])
        return ret

# ret = split_and_sum("0-1-2-3-4-5")
# print(ret)