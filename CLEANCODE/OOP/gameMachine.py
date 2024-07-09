class GameMachine():
    def __init__(self):
        self.__totalCoin: int = 0

    def inputCoin(self, a):
        if a > 5:
            print('ERROR')
            return

        self.__totalCoin += a

        if self.__totalCoin > 10:
            print('ERROR')
            return
    def playGame(self):
        self.__totalCoin -= 1

    def printCoin(self):
        print(self.__totalCoin)


g1 = GameMachine()
g1.inputCoin(7)
g1.playGame()
g1.printCoin()