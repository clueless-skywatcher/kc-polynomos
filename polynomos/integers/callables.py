from polynomos.base_callable import BaseCallable

from polynomos.integers.functions import extended_euclidean

class ExtendedGCD(BaseCallable):
    '''
    Given two integers a and b, calculates the Extended
    GCD of a and b and outputs (gcd, x, y) such that
    a * x + b * y = gcd
    '''
    @staticmethod
    def eval(a, b, **kwargs):
        return extended_euclidean(a, b)