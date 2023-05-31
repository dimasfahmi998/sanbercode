import unittest
from unittest.suite import TestSuite
import cart, base_login

if __name__ == "__main__":
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTest(loader.loadTestsFromModule(base_login))
    suite.addTest(loader.loadTestsFromModule(cart))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
