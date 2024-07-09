from abc import ABCMeta, abstractmethod


class IAzure(metaclass=ABCMeta):
    @abstractmethod
    def ms_connect(self):
        pass

    @abstractmethod
    def ms_login(self, id, pwd):
        pass

    @abstractmethod
    def ms_sendData(self):
        pass

    @abstractmethod
    def ms_receiveData(self):
        pass

    @abstractmethod
    def ms_disconnect(self):
        pass


class Azure(IAzure):
    def ms_connect(self):
        pass

    def ms_login(self, id, pwd):
        pass

    def ms_sendData(self):
        pass

    def ms_receiveData(self):
        pass

    def ms_disconnect(self):
        pass


class AWS:
    def aws_conn(self, id, pwd):
        pass

    def aws_setData(self):
        pass

    def aws_getData(self):
        pass

    def aws_bye(self):
        pass


class Adapter_AWS(IAzure):
    def __init__(self):
        self.aws = AWS()

    def ms_connect(self):
        pass

    def ms_login(self, id, pwd):
        self.aws.aws_conn(id, pwd)

    def ms_sendData(self):
        self.aws.aws_setData()

    def ms_disconnect(self):
        self.aws.aws_bye()

    def ms_receiveData(self):
        self.aws.aws_getData()


def run(az: Azure):
    az.ms_connect()
    az.ms_login('KFC', '1234')
    az.ms_sendData()
    az.ms_disconnect()


def client():
    # run(Azure())
    run(Adapter_AWS)
