import doctest
import unittest

class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')
    
    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')


def average(values):
    """计算一组数字的算术平均数。
    
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)



class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


if __name__ == '__main__':
    doctest.testmod()
    unittest.main

