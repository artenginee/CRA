from abc import ABC, abstractmethod


class Movie(ABC):
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0

    def __init__(self, title: str, price_code):
        self.__title = title
        self.__price_code = price_code

    def get_price_code(self):
        return self.__price_code

    def set_price_code(self, arg):
        self.__price_code = arg

    def get_title(self):
        return self.__title

    @abstractmethod
    def get_charge(self, days_rented):
        pass

    @abstractmethod
    def get_point(self, days_rented):
        pass


class RegularMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.REGULAR)

    def get_charge(self, days_rented):
        this_amount = 2.0
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount

    def get_point(self, days_rented):
        return 1

class ChildrenMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.CHILDRENS)

    def get_charge(self, days_rented):
        this_amount = 1.5
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount

    def get_point(self, days_rented):
        return 1

class NewReleaseMovie(Movie):
    def __init__(self, title: str):
        super().__init__(title, Movie.NEW_RELEASE)

    def get_charge(self, days_rented):
        this_amount = 0.0
        this_amount += days_rented * 3
        return this_amount

    def get_point(self, days_rented):
        if days_rented > 1:
            return 2
        return 1