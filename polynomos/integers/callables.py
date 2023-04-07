from polynomos.base_callable import BaseCallable

from polynomos.integers.functions import (
    extended_euclidean,
    gcd
)

__all__ = [
    "ExtendedGCD",
    "GCD",
    "EvenQ",
    "OddQ",
    "IntQ",
    "DecimalQ",
    "NumQ"
]

class ExtendedGCD(BaseCallable):
    '''
    Given two integers a and b, calculates the Extended
    GCD of a and b and outputs (gcd, x, y) such that
    a * x + b * y = gcd
    '''
    @staticmethod
    def eval(a, b, **kwargs):
        return extended_euclidean(a, b)
    
class GCD(BaseCallable):
    @staticmethod
    def eval(a, b, **kwargs):
        return gcd(a, b)
    
class EvenQ(BaseCallable):
    @staticmethod
    def eval(a: int, **kwargs):
        return a % 2 == 0
    
class OddQ(BaseCallable):
    @staticmethod
    def eval(a: int, **kwargs):
        return a % 2 == 1
    
class IntQ(BaseCallable):
    @staticmethod
    def eval(a: int | float, **kwargs):
        return isinstance(a, int)
    
class DecimalQ(BaseCallable):
    @staticmethod
    def eval(a: int | float, **kwargs):
        return isinstance(a, float)
    
class NumQ(BaseCallable):
    @staticmethod
    def eval(a, **kwargs):
        return isinstance(a, (int, float))