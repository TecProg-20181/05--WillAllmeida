import unittest
from diskspace import bytes_to_readable

class TestMethods(unittest.TestCase):

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")



suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
