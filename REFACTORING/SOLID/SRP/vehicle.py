class Vehicle:
    def __init__(self, max_fuel: int) -> None:
        super().__init__()
        self.__max_fuel = max_fuel
        self.__remaining_fuel = max_fuel

    def get_max_fuel(self):
        return self.__max_fuel

    def get_remaining_fuel(self):
        return self.__remaining_fuel

    def set_remaining_fuel(self, remaining_fuel: int):
        self.__remaining_fuel = remaining_fuel

    def accelerate(self):
        self.__remaining_fuel -= 1


class Fueler:
    def re_fuel(self, vehicle: Vehicle):
        vehicle.set_remaining_fuel(vehicle.get_max_fuel())