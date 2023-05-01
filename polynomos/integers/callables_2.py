from polynomos.base_callable import BaseCallable

from polynomos.integers.functions import partition_integer

__all__ = [
    'IntegerPartitions'
]

class IntegerPartitions(BaseCallable):
    @staticmethod
    def eval(n: int):
        return partition_integer(n)