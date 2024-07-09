import unittest
from abc import ABC, abstractmethod
from enum import Enum


class DrivingMode(Enum):
    SPORT = 0
    COMFORT = 1


class Vehicle:
    def __init__(self) -> None:
        super().__init__()
        self.__power = 0
        self.__suspension_height = 0

    def get_power(self):
        return self.__power

    def get_suspension_height(self):
        return self.__suspension_height

    def set_power(self, power):
        self.__power = power

    def set_suspension_height(self, suspension_height):
        self.__suspension_height = suspension_height


class Mode(ABC):
    @abstractmethod
    def change_mode(self, __vehicle):
        pass


class SportMode(Mode):

    def change_mode(self, vehicle: Vehicle):
        vehicle.set_power(500)
        vehicle.set_suspension_height(10)


def create_mode(driving_mode: DrivingMode):
    if driving_mode == DrivingMode.SPORT:
        mode = SportMode()
    elif driving_mode == DrivingMode.COMFORT:
        mode = ComfortMode()
    else:
        mode = NormalMode()
    return mode


class EventHandler:
    def __init__(self, vehicle: Vehicle) -> None:
        super().__init__()
        self.__vehicle = vehicle

    def change_driving_mode(self, driving_mode: DrivingMode):
        mode = create_mode(driving_mode)
        mode.change_mode(self.__vehicle)

        # when we need to add another mode (e.g. ECONOMY) 2 classes will change DrivingMode and EventHandler.


class TestEventHandler(unittest.TestCase):
    def test_something(self):
        my_v = Vehicle()
        handler = EventHandler(my_v)

        handler.change_driving_mode(DrivingMode.SPORT)

        self.assertEqual(my_v.get_power(), 500)
        self.assertEqual(my_v.get_suspension_height(), 10)