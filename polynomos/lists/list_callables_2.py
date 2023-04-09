from polynomos.base_callable import BaseCallable
from polynomos.fractions.callables import Fraction, NumericValue
from polynomos.fractions.rational import Rational
from polynomos.lists.plainlist import PlainList
from polynomos.lists.list_callables_0 import ListLength

__all__ = [
    "ListCount",
    "Range",
    "Subdivide",
    "Prepend",
    "Append",
    "Insert"
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
    
class Subdivide(BaseCallable):
    @staticmethod
    def eval(n, interval: None | int | float | Rational | tuple | PlainList = None, float_result: bool = False, **kwargs):
        if interval is None:
            final_list = [Fraction(x, n) for x in range(n + 1)]
        if isinstance(interval, (int, float, Rational)):
            final_list = [x * Fraction(interval, n) for x in range(n + 1)]
        if isinstance(interval, tuple):
            interval = PlainList(*interval)
        if isinstance(interval, PlainList):
            if ListLength(interval) != 2:
                raise ValueError("`interval` must either have a number or a PlainList/tuple of 2 numbers")
            max_interval = max(interval[0], interval[1])
            min_interval = min(interval[0], interval[1])
            final_list = [min_interval + x * Fraction(max_interval - min_interval, n) for x in range(n + 1)]

            if interval[1] < interval[0]:
                final_list = final_list[::-1]

        if float_result:
            final_list = [NumericValue(x) for x in final_list]
        return PlainList(*final_list)

class Prepend(BaseCallable):
    @staticmethod
    def eval(l: PlainList, e):
        return l.prepend(e)
    
class Append(BaseCallable):
    @staticmethod
    def eval(l: PlainList, e):
        return l.append(e)
    
class Insert(BaseCallable):
    @staticmethod
    def eval(l: PlainList, e, position: int):
        return l.insert(e, position)
    