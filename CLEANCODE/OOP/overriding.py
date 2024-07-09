from typing import override


class Phone:
    def __init__(self):
        pass

    def call(self):
        print('Calling...')


class SmartPhone(Phone):
    def __init__(self):
        super().__init__()

    @override
    def call(self):
        print('SmartCalling...')


s1 = SmartPhone()
s1.call()
