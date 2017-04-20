class maxminobj(object):
    pass

import unittest
from app.maxmin import max_val, min_val, print_usage


class maxminTestCase(unittest.TestCase)

    def test_max_val(self):
        retorno = self.maxminobj = max_val(2,6)
        self.assertEquals(retorno,6)

    def test_min_val(self):
        retorno = self.maxminobj = min_val(2, 6)
        self.assertEquals(retorno, 2)

if __name__ == '__main__':
    unittest.main()