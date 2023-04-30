from polynomos.base_callable import BaseCallable
from polynomos.combinomos.permutations import _get_combinations, _get_permutations
from polynomos.lists.plainlist import PlainList

__all__ = [
    'Permutations',
    'Combinations'
]

class Permutations(BaseCallable):
    @staticmethod
    def eval(iterable: str | PlainList, **kwargs):
        perms = _get_permutations(list(iterable))
        if isinstance(iterable, str):
            return PlainList(*[''.join(perm) for perm in perms])
        return PlainList(*[PlainList(*perm) for perm in perms])
    
class Combinations(BaseCallable):
    @staticmethod
    def eval(iterable: str | PlainList, k: int, **kwargs):
        combs = _get_combinations(list(iterable), k)
        if isinstance(iterable, str):
            return PlainList(*[''.join(comb) for comb in combs])
        return PlainList(*[PlainList(*comb) for comb in combs])