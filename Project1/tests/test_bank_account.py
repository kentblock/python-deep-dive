import unittest
import sys
sys.path.insert(0, '..')
from bank_account import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def get_default_account(first_name="first name", last_name="last name", account_num=123, balance=None):
    if balance:
        return BankAccount(account_num, first_name, last_name, balance)
    return BankAccount(account_num, first_name, last_name)

class TestAccount(unittest.TestCase):

    def test_create_account_success(self):
        """Test creating BankAccount object is successful"""
        first_name = "first name"
        last_name = "last name"
        account_num = 123
        account = BankAccount(account_num, first_name, last_name)
        self.assertEqual(first_name, account.first_name)
        self.assertEqual(last_name, account.last_name)
        self.assertEqual(account_num, account.account_num)
        self.assertEqual(0 , account.balance)

    def test_create_account_fail(self):
        """Test creating account with invalid arguments fails"""
        self.assertRaises(TypeError, BankAccount, "account number", "first name", "last name")
        self.assertRaises(TypeError, BankAccount, 123, 1234, "last name")
        self.assertRaises(TypeError, BankAccount, 123, "first name", 1234)
        self.assertRaises(TypeError, BankAccount, 123, "first name", "last name", "1000")
        self.assertRaises(TypeError, BankAccount, 123, "first name", "last name", 1000, "timezone")

    def test_deposit_success(self):
        """Test depositing money into account"""
        account = get_default_account()
        deposit_amount = 1000
        account.deposit(deposit_amount)
        self.assertEqual(account.balance, deposit_amount)

    def test_deposit_fail(self):
        """Test making invalid deposits fails"""
        account = get_default_account()
        self.assertRaises(TypeError, account.deposit, "deposit")

    def test_withdraw_success(self):
        """Test withdrawing from the account"""
        balance = 1000
        account = get_default_account(balance=balance)
        withdraw_amount = 1000
        account.withdraw(withdraw_amount)
        self.assertEqual(balance - withdraw_amount, account.balance)

    def test_withdraw_fail(self):
        """Test withdrawing invalid amount fails"""
        balance = 1000
        account = get_default_account(balance=balance)
        self.assertRaises(ValueError, account.withdraw, balance + 1)
        self.assertRaises(TypeError, account.withdraw, "balance")

    def test_pay_interest(self):
        """Test paying interest function"""
        balance = 1000
        account = get_default_account(balance=balance)
        interest_rate = account.get_int_rate()
        account.pay_interest()
        self.assertEqual(account.balance, balance - balance * interest_rate)

    def test_changing_rate_all_accounts(self):
        """Test changing the interest rate changes them for each account"""
        account1 = get_default_account()
        account2 = get_default_account()
        account1.set_int_rate(4.5)
        self.assertEqual(account1.get_int_rate(), account2.get_int_rate())

    def test_parse_confirmation_code(self):
        pass


if __name__ == "__main__":
    run_tests(TestAccount)