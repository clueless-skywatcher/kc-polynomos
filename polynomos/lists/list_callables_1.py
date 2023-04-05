from polynomos.base_callable import BaseCallable
from polynomos.lists.plainlist import PlainList
from polynomos.lists.list_callables_0 import ListLength, PlainListNew

__all__ = [
    "ElementAt",
    "First",
    "Last",
    "Middle"
]

class ElementAt(BaseCallable):
    @staticmethod
    def eval(l: PlainList, i: int, **kwargs):
        if i >= ListLength(l):
            raise ValueError(f"Index {i} is out of bounds")
        return l[i]

class First(BaseCallable):
    @staticmethod
    def eval(l: PlainList, **kwargs):
        if ListLength(l) == 0:
            return None
        return l[0]
    
class Last(BaseCallable):
    @staticmethod
    def eval(l: PlainList, **kwargs):
        if ListLength(l) == 0:
            return None
        return l[ListLength(l) - 1]
    
class Middle(BaseCallable):
    @staticmethod
    def eval(l: PlainList, **kwargs):
        length = ListLength(l)

        if length == 0:
            return None
        elif length % 2:
            return l[length // 2]
        return PlainListNew(l[(length // 2) - 1], l[length // 2])