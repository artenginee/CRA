class Calculator():
    def __init__(self):
        self.result = 0

    def plus(self, a, b):
        self.result = a + b

    def minus(self, a, b):
        self.result = a - b

    def multiple(self, a, b):
        self.result = a * b

    def divide(self, a, b):
        self.result = a / b

    def printResult(self):
        print(self.result)


c1 = Calculator()
c1.plus(1, 2)
c1.minus(1, 2)
c1.multiple(1, 2)
c1.divide(1, 2)
c1.printResult()