from diskspace import bytes_to_readable, subprocess_check_output, print_tree
import os
import unittest
from io import StringIO
import sys

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.largest_size = 8
        self.total_size = 4
        self.cmd = 'du '
        self.path = os.path.abspath('.')
        self.cmd += self.path
        

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_bytes_to_readable_wrong(self):
        blocks = 100
        self.assertNotEqual(bytes_to_readable(blocks), "50.00Mb")

    def test_subprocess_check_output(self):
        path = subprocess_check_output(self.cmd)
        self.assertIn(self.path, path)




suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
