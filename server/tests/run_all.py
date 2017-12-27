import sys
import os
from unittest import TestLoader, TextTestRunner, TestSuite

sys.path.insert(0, os.path.dirname('../'))

from tests.api.app_tests import FlaskTestCase


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(FlaskTestCase)
        ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

