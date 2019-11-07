#!/usr/bin/env python3
import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
    jiben ceshilei
    """
    def test_fact(self):
        """
        shiji ceshi
        """
        res = fact(5)
        self.assertEqual(res,120)

    def test_error(self):
        """
        cuowu yinfa yichang
        """
        self.assertRaises(ZeroDivisionError.div,0)

if __name__ == '__main__':
    unittest.main()
