import numpy as np


class Rule(object):
    """Standard Deviation Rules 68%, 95% Variant"""

    STANDARD_DEVIATION_RANGE = 2
    MAX_VALUE = 100
    MIN_VALUE = 0
    cleanMax = (lambda self, x: self.MAX_VALUE if x >= self.MAX_VALUE else x)
    cleanMin = (lambda self, x: self.MIN_VALUE if x <= self.MIN_VALUE else x)
    clean = (lambda self, x: self.cleanMax(self.cleanMin(x)))

    def __init__(self, average, root_mean_square_deviation):
        self.min68 = self.clean(average - root_mean_square_deviation)
        self.max68 = self.clean(average + root_mean_square_deviation)
        self.min95 = self.clean(average - self.STANDARD_DEVIATION_RANGE * root_mean_square_deviation)
        self.max95 = self.clean(average + self.STANDARD_DEVIATION_RANGE * root_mean_square_deviation)


class StandardDeviation(object):
    """Standard Deviation Object"""

    def __init__(self, x, y):
        if len(x) != len(y):
            raise Exception("x length={}, y length={} is same length.".format(len(x), len(y)))

        total = len(x)
        x_average = np.average(x)
        y_average = np.average(y)

        if x_average != y_average:
            raise Exception("x average={}, y average={} is same average.".format(x_average, y_average))

        x_root_mean_square_deviation = np.sqrt(np.sum(np.square(x - x_average)) / total)
        y_root_mean_square_deviation = np.sqrt(np.sum(np.square(y - y_average)) / total)
        self.x_rule = Rule(x_average, x_root_mean_square_deviation)
        self.y_rule = Rule(y_average, y_root_mean_square_deviation)

    def variant_printer(self):
        print "> x case: "
        print "About 68% in {} ~ {} points".format(np.round(self.x_rule.min68, 1), np.round(self.x_rule.max68, 1))
        print "About 95% in {} ~ {} points".format(np.round(self.x_rule.min95, 1), np.round(self.x_rule.max95, 1))
        print "> y case: "
        print "About 68% in {} ~ {} points".format(np.round(self.y_rule.min68, 1), np.round(self.y_rule.max68, 1))
        print "About 95% in {} ~ {} points".format(np.round(self.y_rule.min95, 1), np.round(self.y_rule.max95, 1))