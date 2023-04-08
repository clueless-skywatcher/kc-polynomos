from polynomos.base_callable import BaseCallable
from polynomos.fractions.rational import Rational

__all__ = [
    "Fraction",
    "NumericValue",
    "Rationalize"
]

class Fraction(BaseCallable):
    @staticmethod
    def eval(num: int, denom: int, auto_reduce = True, **kwargs):
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if num == 0:
            return 0
        if denom == -1:
            return -num
        if denom == 1:
            return num
        if num % denom == 0:
            return num // denom
        return Rational(num, denom, auto_reduce = auto_reduce)

class NumericValue(BaseCallable):
    @staticmethod
    def eval(x: Rational | int | float, n: int = 10):
        if isinstance(x, (int, float)):
            return round(x, n)
        return round(float(x.num / x.denom), n)
    
class Rationalize(BaseCallable):
    @staticmethod
    def eval(x: float, **kwargs):
        return Rational.rationalize(x)