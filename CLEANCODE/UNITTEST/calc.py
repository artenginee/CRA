class Calc:
    def get_sum(self, a, b):
        return a + b

    def getAbsSum(self, lst:list) -> list:
        ret = list()
        for t in lst:
            ret.append(abs(t))
        return ret