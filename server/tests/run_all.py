from unittest import TestLoader, TextTestRunner, TestSuite
from tests.api.test_app import AppTestCase


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(AppTestCase)
        ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

