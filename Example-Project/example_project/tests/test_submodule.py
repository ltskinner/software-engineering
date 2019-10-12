import unittest

import sys, os
testdir = os.path.dirname(__file__)
#srcdir = '../antigravity'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, '..')))

from example_project.subpackage import sub_module_function


class TestSum(unittest.TestCase):

    def test_submodule(self):
        res = sub_module_function()
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
