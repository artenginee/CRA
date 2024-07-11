class Cal:
    def get_sum(self,a,b):
        return a+b

    def say_hi(self):
        return 'HI'

    def say_hello(self):
        return 'HELLO'

    def get_gop_three(self, a, b):
        t1 = self.get_sum(a,b)
        t2 = self.get_sum(a, b)
        t3 = self.get_sum(a, b)
        return t1 + t2 + t3