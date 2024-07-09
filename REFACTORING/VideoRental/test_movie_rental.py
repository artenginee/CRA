from unittest import TestCase

from REFACTORING.VideoRental.movie import RegularMovie, NewReleaseMovie, ChildrenMovie
from customer import Customer, Rental, Movie

TITLE = 'TITLE_NOT_IMPORTANT'

NAME = 'NAME_NOT_IMPORTANT'


class Tests(TestCase):
    # def test_sample(self):
    #     customer = Customer("Bob")
    #     customer.add_rental(Rental(Movie("Jaws", Movie.REGULAR), 2))
    #     customer.add_rental(Rental(Movie("Golden Eye", Movie.REGULAR), 3))
    #     customer.add_rental(Rental(Movie("Short New", Movie.NEW_RELEASE), 1))
    #     customer.add_rental(Rental(Movie("Long New", Movie.NEW_RELEASE), 2))
    #     customer.add_rental(Rental(Movie("Bambi", Movie.CHILDRENS), 3))
    #     customer.add_rental(Rental(Movie("Toy Story", Movie.CHILDRENS), 4))
    #
    #     expected = "Rental Record for Bob\n"
    #     expected += "\tJaws\t2.0\n"
    #     expected += "\tGolden Eye\t3.5\n"
    #     expected += "\tShort New\t3.0\n"
    #     expected += "\tLong New\t6.0\n"
    #     expected += "\tBambi\t1.5\n"
    #     expected += "\tToy Story\t3.0\n"
    #     expected += "Amount owed is 19.0\n"
    #     expected += "You earned 7 frequent renter points"
    #
    #     print(repr(customer.statement()))
    #     self.assertEqual(expected, customer.statement())

    # 'Rental Record for Bob\n
    # \tJaws\t2.0\n\tGolden Eye\t3.5\n
    # \tShort New\t3.0\n
    # \tLong New\t6.0\n
    # \tBambi\t1.5\n
    # \tToy Story\t3.0\n
    # Amount owed is 19.0\n
    # You earned 7 frequent renter points'
    def setUp(self):
        super().setUp()
        self.customer = Customer(NAME)

    def get_movie(self, price_code):
        if price_code == Movie.REGULAR:
            return RegularMovie(TITLE)
        elif price_code == Movie.NEW_RELEASE:
            return NewReleaseMovie(TITLE)
        elif price_code == Movie.CHILDRENS:
            return ChildrenMovie(TITLE)
        else:
            return None

    def test_return_new_customer(self):
        self.assertIsNotNone(self.customer)

    def test_statement_for_no_rental(self):
        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + 'Amount owed is 0\n'
                         + 'You earned 0 frequent renter points')

    def test_statement_for_regular_movie_rental(self):
        self.customer.add_rental(self.create_rental_for(2, Movie.REGULAR))

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + 'Amount owed is 2.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie(self):
        self.customer.add_rental(self.create_rental_for(1, Movie.NEW_RELEASE))

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_3_days(self):
        self.customer.add_rental(self.create_rental_for(4, Movie.CHILDRENS))

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 3.0\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_childrens_movie_rental_more_than_4_days(self):
        self.customer.add_rental(self.create_rental_for(3, Movie.CHILDRENS))

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t1.5\n'
                         + 'Amount owed is 1.5\n'
                         + 'You earned 1 frequent renter points')

    def test_statement_for_new_release_movie_rental_more_than_1_days(self):
        rental = self.create_rental_for(2, Movie.NEW_RELEASE)
        self.customer.add_rental(rental)

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t6.0\n'
                         + 'Amount owed is 6.0\n'
                         + 'You earned 2 frequent renter points')

    def create_rental_for(self, days_rented, price_code):
        movie = self.get_movie(price_code)
        rental = Rental(movie, days_rented)
        return rental

    def test_statement_for_few_movie_rental(self):
        regular_movie = self.get_movie(Movie.REGULAR)
        new_release_movie = self.get_movie(Movie.NEW_RELEASE)
        childrens_movie = self.get_movie(Movie.CHILDRENS)
        self.customer.add_rental(Rental(regular_movie, 1))
        self.customer.add_rental(Rental(new_release_movie, 4))
        self.customer.add_rental(Rental(childrens_movie, 4))

        self.assertEqual(self.customer.statement(),
                         'Rental Record for NAME_NOT_IMPORTANT\n'
                         + '\tTITLE_NOT_IMPORTANT\t2.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t12.0\n'
                         + '\tTITLE_NOT_IMPORTANT\t3.0\n'
                         + 'Amount owed is 17.0\n'
                         + 'You earned 4 frequent renter points')