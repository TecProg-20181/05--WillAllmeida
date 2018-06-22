from diskspace import bytes_to_readable, subprocess_check_output
import os
import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.largest_size = 8
        self.total_size = 4
        self.cmd = 'du '
        self.abs_directory = os.path.abspath('.')
        self.cmd += self.abs_directory
        self.file_tree = {self.abs_directory: {'print_size': '50.00Kb', 'children': [], 'size': 8}}

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_subprocess_check_output(self):
        path = subprocess_check_output(self.cmd)
        self.assertIn(self.abs_directory, path)


suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
