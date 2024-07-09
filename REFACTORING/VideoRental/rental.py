from movie import Movie


class Rental:
    def __init__(self, movie: Movie, daysRented: int):
        self.__days_rented = daysRented
        self.__movie: Movie = movie

    def get_days_rented(self):
        return self.__days_rented

    def get_movie(self):
        return self.__movie

    def get_charge(self):
        return self.__movie.get_charge(self.get_days_rented())

    def get_point(self):
        return self.__movie.get_point(self.get_days_rented())