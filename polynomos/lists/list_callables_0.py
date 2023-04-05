from polynomos.base_callable import BaseCallable
from polynomos.lists.plainlist import PlainList

__all__ = [
    'ListLength',
    'PlainListNew'
]

class ListLength(BaseCallable):
    @staticmethod
    def eval(l: PlainList, **kwargs):
        return l.length
    
class PlainListNew(BaseCallable):
    @staticmethod
    def eval(*args, **kwargs):
        return PlainList(*args, **kwargs)