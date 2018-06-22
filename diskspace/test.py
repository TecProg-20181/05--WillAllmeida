from diskspace import bytes_to_readable, subprocess_check_output, show_space_list, args, print_tree
import os
import unittest
import StringIO
import sys


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.largest_size = 8
        self.total_size = 4
        self.cmd = 'du '
        self.path = os.path.abspath('.')
        self.cmd += self.path
        self.file_tree = {self.path: {'print_size': '50.00Kb', 'children': [], 'size': 3}}

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_bytes_to_readable_wrong(self):
        blocks = 100
        self.assertNotEqual(bytes_to_readable(blocks), "50.00Mb")

    def test_subprocess_check_output(self):
        path = subprocess_check_output(self.cmd)
        self.assertIn(self.path, path)

    def test_print_tree(self):
            capturedOutput = StringIO.StringIO()
            sys.stdout = capturedOutput
            print_tree(self.file_tree, self.file_tree[self.path], self.path,
                       self.largest_size, self.total_size)
            sys.stdout = sys.__stdout__
            self.assertEqual('50.00Kb   75%  '+self.path, capturedOutput.getvalue().strip())

    def test_show_space_list(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        show_space_list(args.directory, args.depth, order=(args.order == 'desc'))
        sys.stdout = sys.__stdout__
        self.assertIn('Size (%) File' and self.path, capturedOutput.getvalue().strip())



suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
