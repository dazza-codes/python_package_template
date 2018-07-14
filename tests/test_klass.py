import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from module_name import Klass

class TestKlass(unittest.TestCase):

    def setUp(self):
        super()
        self.klass = Klass()

    def test_init(self):
        self.assertIsInstance(self.klass, Klass)


if __name__ == '__main__':
    unittest.main()

