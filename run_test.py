from tests import *
import unittest


def run_tests():
    # Create a test suite
    suite = unittest.TestSuite()
    # Add all tests to the test suite
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestEvent))
    suite.addTest(loader.loadTestsFromTestCase(TestOwner))
    suite.addTest(loader.loadTestsFromTestCase(TestHive))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    run_tests()
