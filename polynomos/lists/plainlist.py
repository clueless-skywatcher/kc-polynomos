from polynomos.fractions.rational import Rational

class PlainList:
    def __init__(self, *args, **kwargs) -> None:
        self._list = list(args)
        self._kwargs = kwargs

    @property
    def length(self):
        return len(self._list)

    def __add__(self, other):
        if isinstance(other, (int, float, Rational)):
            return PlainList(*map(lambda x: x + other, self._list))
        elif isinstance(other, PlainList):
            if self.length == other.length:
                return PlainList(*[x + y for x, y in zip(self._list, other._list)])
            raise ValueError("Cannot add two PlainLists with different lengths")
        else:
            raise TypeError("Lists can only be added to numbers and same-sized lists")
        
    def prepend(self, e):
        x = [e] + self._list
        return PlainList(*x)
    
    def append(self, e):
        x = self._list + [e]
        return PlainList(*x)
    
    def insert(self, e, position: int):
        if position >= len(self._list):
            raise ValueError(f"Given position {position} is out of bounds")
        x = self._list[:position] + [e] + self._list[position:]
        return PlainList(*x)
        
    def __eq__(self, other):
        if not isinstance(other, PlainList):
            raise TypeError
        return self._list == other._list
        
    def __getitem__(self, i):
        return self._list[i]
        
    def __str__(self) -> str:
        return str(self._list)
    
    def __repr__(self) -> str:
        return str(self._list)