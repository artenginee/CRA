class Calc:
    def cal_minus(self, a, b):
        if a < b:
            return self.cal_minus(b, a)

        return a - b

    def fibo(self, n):
        if n == 2 or n == 1:
            return 1
        return self.fibo(n-1) + self.fibo(n-2)
