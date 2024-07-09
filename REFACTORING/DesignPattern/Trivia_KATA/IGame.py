from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    @abstractmethod
    def add(self, player_name):
        pass

    @abstractmethod
    def rolling(self, roll):
        pass

    @abstractmethod
    def was_correctly_answered(self):
        pass

    @abstractmethod
    def wrong_answer(self):
        pass
