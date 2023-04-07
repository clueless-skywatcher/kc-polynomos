from polynomos.base_callable import BaseCallable
from polynomos.lists.plainlist import PlainList
from polynomos.lists.list_callables_0 import ListLength

__all__ = [
    "ListCount",
    "Range"
]

class ListCount(BaseCallable):
    @staticmethod
    def eval(l: PlainList, elem, **kwargs):
        return sum([l[i] == elem for i in range(ListLength(l))])
    
class Range(BaseCallable):
    @staticmethod
    def eval(n: int, m: int | None = None, step: int | None = None, **kwargs):
        if step is not None:
            if m is not None:
                if m <= 0:
                    return PlainList(*list(range(n, m - 1, step)))
                return PlainList(*list(range(n, m + 1, step)))
            else:
                return PlainList(*list(range(1, n + 1, step)))
        else:
            if m is not None:
                if m <= 0:
                    return PlainList(*list(range(n, m - 1)))
                return PlainList(*list(range(n, m + 1)))
        
        return PlainList(*list(range(1, n + 1)))