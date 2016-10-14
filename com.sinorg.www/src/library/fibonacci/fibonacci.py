class Fibonacci(object):
    """Fibonacci function."""

    def __init__(self):
        print 'Fibonacci'

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 2) + self.fibonacci(n - 1)
