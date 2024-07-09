class Account:
    def __init__(self, money) -> None:
        super().__init__()
        self.__balance = money

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        self.__balance -= money