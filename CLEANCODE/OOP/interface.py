from abc import ABC, abstractmethod


class Socket(ABC):
    @abstractmethod
    def plugin(self):
        pass

    @abstractmethod
    def unplug(self):
        pass

class Samsang(Socket):
    def plugin(self):
        pass

    def unplug(self):
        pass

    def enable330V(self):
        pass

    def disable330V(self):
        pass


class SunPower(Socket):

    def plugin(self):
        pass

    def unplug(self):
        pass

    def enableSun(self):
        pass

    def disableSun(self):
        pass

a = Samsang()
