import unittest
import numpy as np
import standard_deviation as sd


class MyTestCase(unittest.TestCase):
    TEST_CASE_X = np.array([35, 37, 59, 59, 59, 60, 65, 70])
    TEST_CASE_Y = np.array([0, 8, 62, 65, 67, 70, 80, 92])
    ANSWER_X = np.array([43.7, 67.3, 31.8, 79.2])
    ANSWER_Y = np.array([24.4, 86.6, 0, 100])

    def test_something(self):
        s = sd.StandardDeviation(self.TEST_CASE_X, self.TEST_CASE_Y)
        self.assertEqual(self.ANSWER_X[0], np.round(s.x_rule.min68, 1))
        self.assertEqual(self.ANSWER_X[1], np.round(s.x_rule.max68, 1))
        self.assertEqual(self.ANSWER_X[2], np.round(s.x_rule.min95, 1))
        self.assertEqual(self.ANSWER_X[3], np.round(s.x_rule.max95, 1))
        self.assertEqual(self.ANSWER_Y[0], np.round(s.y_rule.min68, 1))
        self.assertEqual(self.ANSWER_Y[1], np.round(s.y_rule.max68, 1))
        self.assertEqual(self.ANSWER_Y[2], np.round(s.y_rule.min95, 1))
        self.assertEqual(self.ANSWER_Y[3], np.round(s.y_rule.max95, 1))


if __name__ == '__main__':
    unittest.main()