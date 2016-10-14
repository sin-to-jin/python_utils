import unittest

import numpy as np

import fibonacci

ANSWER_DATA = np.array(
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946])
TEST_DATA = np.array(range(22))
F = fibonacci.Fibonacci()
f = lambda x: F.fibonacci(x)


class MyTestCase(unittest.TestCase):
    def test_fibonacci(self):
        for x in TEST_DATA:
            self.assertEqual(f(x), ANSWER_DATA[x])


if __name__ == '__main__':
    unittest.main()
