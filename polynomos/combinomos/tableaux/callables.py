from polynomos.base_callable import BaseCallable
from polynomos.combinomos.tableaux.funcs import (
    ferrers_diagram,
    partition_transpose,
    durfee_square
)
from polynomos.lists.plainlist import PlainList

__all__ = [
    'FerrersDiagram',
    'TransposePartition',
    'DurfeeSquare'
]

class FerrersDiagram(BaseCallable):
    @staticmethod
    def eval(l: PlainList, notation: str = 'english', character: str = '*', **kwargs):
        if not all([isinstance(l[i], int) and l[i] > 0 for i in range(len(l))]):
            raise ValueError("All values must be positive integers")
        if notation not in ['english', 'french']:
            raise ValueError("'notation' value must be 'english' or 'french'")
        if len(character) != 1:
            raise ValueError("'character' must be a single character")
        diagram = ferrers_diagram(l, notation, character)
        print(diagram)
        return diagram
    
class TransposePartition(BaseCallable):
    @staticmethod
    def eval(l: PlainList, *args, **kwargs):
        return partition_transpose(l)
    
class DurfeeSquare(BaseCallable):
    @staticmethod
    def eval(l: PlainList, *args, **kwargs):
        return durfee_square(l)
