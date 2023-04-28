from polynomos.base_callable import BaseCallable
from polynomos.combinomos.permutations import _get_permutations
from polynomos.lists.plainlist import PlainList

__all__ = [
    'Permutations'
]

class Permutations(BaseCallable):
    @staticmethod
    def eval(iterable: str | PlainList, **kwargs):
        perms = _get_permutations(list(iterable))
        if isinstance(iterable, str):
            return PlainList(*[''.join(perm) for perm in perms])
        return PlainList(*perms)