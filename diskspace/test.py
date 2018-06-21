import unittest
from diskspace import bytes_to_readable, subprocess_check_output
import subprocess

class TestMethods(unittest.TestCase):

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_subprocess_check_output(self):
        path = "/test/"
        self.assertEqual(subprocess_check_output(path),['/test'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
