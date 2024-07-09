from rental import Rental
from movie import Movie

class Customer:
    def __init__(self, name: str):
        self.__rentals = []
        self.__name = name

    def get_name(self):
        return self.__name

    def statement(self):

        # headline
        result = "Rental Record for " + self.get_name() + "\n"

        # midlines
        for a_rental in self.__rentals:
            result += "\t" + a_rental.get_movie().get_title() + "\t" + str(a_rental.get_charge()) + "\n"

        # add footer lines
        result += "Amount owed is " + str(self.get_total_amount()) + "\n"
        result += "You earned " + str(self.get_total_points()) + " frequent renter points"

        return result

    def get_total_amount(self):
        result = 0
        for a_rental in self.__rentals:
            result += a_rental.get_charge()
        return result

    def get_total_points(self):
        frequent_renter_points = 0
        for a_rental in self.__rentals:
            frequent_renter_points += a_rental.get_point()
        return frequent_renter_points

    def add_rental(self, param: Rental):
        self.__rentals.append(param)