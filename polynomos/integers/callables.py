from polynomos.base_callable import BaseCallable

from polynomos.integers.functions import extended_euclidean

class ExtendedEuclideanGCD(BaseCallable):
    @staticmethod
    def eval(a, b, **kwargs):
        return extended_euclidean(a, b)