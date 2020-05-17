import unittest
import sys
sys.path.insert(0, '..')
from bank_account import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class TestAccount(unittest.TestCase):




if __name__ == "__main__":
    run_tests(TestAccount)