from abc import abstractmethod, ABC


class Factory:
    def __init__(self):
        pass

    def create_doll(self, name: str):
        if name == 'red':
            return RedDoll()
        elif name == 'blue':
            return BlueDoll()
        else:
            pass


class Doll(ABC):
    @abstractmethod
    def push(self):
        pass


class BlueDoll(Doll):
    def push(self):
        print('BlueDoll')


class RedDoll(Doll):
    def push(self):
        print('RedDoll')


factory = Factory()
doll = factory.create_doll('blue')
doll.push()
