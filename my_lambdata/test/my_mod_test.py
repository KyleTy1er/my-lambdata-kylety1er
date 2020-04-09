
import unittest

from my_lambdata.my_mod2 import dock_tester

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(dock_tester(3), 6)

if __name__ == '__main__':
    unittest.main()