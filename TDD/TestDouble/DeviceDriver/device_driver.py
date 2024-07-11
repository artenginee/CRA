import time

from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self.__device = device

    def write(self, address: int, data: int) -> None:
        if self.__device.read(address) != 0xFF:
            raise Exception('WriteFailException')

        self.__device.write(address, data)

    def read(self, address: int) -> int:
        result = 0x0
        lst = []
        for i in range(5):
            result = self.__device.read(address)
            if i == 0:
                lst.append(result)
            else:
                if lst[i - 1] == result:
                    lst.append(result)
                else:
                    raise Exception('ReadFailException')

            time.sleep(0.2)

        return result

    def read_and_print(self, start_addr: int, end_addr: int) -> str:
        pass

    def write_all(self, value: int) -> None:
        pass
