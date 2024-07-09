from unittest import TestCase
from account import Account


class TestAccount(TestCase):
    def setUp(self):
        super().setUp()
        self.account = Account(10000)

    def test_create_account(self):
        self.assertIsNotNone(self.account)

    def test_account_init_10000_won(self):
        self.assertEqual(10000, self.account.get_balance())

    def test_deposit_and_confirmation(self):
        self.account.deposit(500)
        self.assertEqual(10500, self.account.get_balance())

    def test_withdraw_and_confirmation(self):
        self.account.withdraw(600)
        self.assertEqual(9400, self.account.get_balance())
