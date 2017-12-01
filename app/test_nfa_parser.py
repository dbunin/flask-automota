import unittest
from nfa_parser import NFA_Parser


class Test_NFA_Parser(unittest.TestCase):
    """
    To run:
        python test_nfa_parser.py
    """
    def test_compile_fail_case(self):
        parser = NFA_Parser()
        with self.assertRaises(Exception) as context:
            parser.compile('a&b')


if __name__ == '__main__':
    unittest.main()
